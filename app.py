import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gerador DUA", page_icon="🤖", layout="centered")

st.title("🤖 Gerador de Atividades Adaptadas (DUA)")
st.write("Crie folhas de atividades acessíveis prontas para copiar ou abrir no Word usando Inteligência Artificial!")

# Campo secreto para o professor colar a chave do Gemini
api_key = st.sidebar.text_input("Cole sua Google API Key aqui:", type="password")

tema = st.text_input("Tema da Aula:", "Substantivo")
perfil = st.selectbox("Perfil de Adaptação:", ["TDAH", "Autismo (TEA)", "Deficiência Intelectual"])
conteudo_extra = st.text_area("Texto base ou instruções adicionais (opcional):")

if st.button("✨ Gerar Atividade com Inteligência Artificial"):
    if not api_key:
        st.error("⚠️ Por favor, cole sua Google API Key na barra lateral esquerda para ativar a IA!")
    else:
        with st.spinner("🤖 A inteligência artificial está criando e adaptando sua atividade... Aguarde!"):
            try:
                # Configura a IA do Google com a sua chave
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Monta o comando pedagógico estrito para a IA
                prompt = f"""
                Você é um psicopedagogo especialista em educação especial, neurodivergências e inclusão escolar, aplicando as diretrizes do Desenho Universal para a Aprendizagem (DUA).
                
                Crie uma folha de atividade escolar completa e adaptada sobre o tema: "{tema}".
                O perfil do aluno é: {perfil}.
                Instruções extras do professor: {conteudo_extra}.
                
                Estrutura obrigatória que você deve retornar:
                ==================================================
                ATIVIDADE ESCOLAR ADAPTADA (DIRETRIZES DUA)
                Nome do Aluno: ____________________________________
                Data: ___/___/_____
                Perfil de Inclusão: {perfil}
                Tema da Aula: {tema}
                ==================================================
                
                1. RESUMO ACESSÍVEL (Sintetize o conteúdo in frases curtas. Se for TDAH, use listas com tópicos e marque em CAIXA ALTA as palavras mais importantes. Se for Autismo, use linguagem totalmente literal e direta, sem metáforas. Se for Deficiência Intelectual, use termos muito simples e concretos do cotidiano).
                
                2. ESPAÇO VISUAL (Escreva apenas uma linha indicando onde o professor deve colocar uma imagem explicativa, ex: [ ESPAÇO VISUAL: Cole aqui uma imagem lúdica de um... ]).
                
                3. EXERCÍCIO DE FIXAÇÃO (Crie uma questão de múltipla escolha com apenas duas opções claras (A e B), com baixa carga cognitiva e foco no objetivo principal do tema).
                """
                
                # Envia para o Gemini resolver
                model = genai.GenerativeModel('gemini-pro')response = model.generate_content(prompt)
                response = model.generate_content(prompt)
                texto_final = response.text


                st.markdown("---")
                st.subheader("📋 Atividade Adaptada Gerada:")
                
                # Mostra na tela
                st.text_area("Texto completo para copiar:", value=texto_final, height=400)
                
                # Botão para baixar para o Word
                st.download_button(
                    label="📥 Baixar Atividade para o Word (.txt)",
                    data=texto_final,
                    file_name=f"Atividade_Adaptada_{perfil}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Erro ao gerar com a IA: {e}")
