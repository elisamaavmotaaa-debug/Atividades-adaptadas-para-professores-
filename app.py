import streamlit as st

st.set_page_config(page_title="Gerador DUA", page_icon="🤖", layout="centered")

st.title("🤖 Gerador de Atividades Adaptadas (DUA)")
st.write("Crie folhas de atividades acessíveis prontas para copiar ou abrir no Word!")

tema = st.text_input("Tema da Aula:", "Povos da Antiguidade: Sumérios e Fenícios")
perfil = st.selectbox("Perfil de Adaptação:", ["TDAH", "Autismo (TEA)", "Deficiência Intelectual"])
conteudo = st.text_area("Texto base ou instruções adicionais (opcional):")

# Lógica de montagem estruturada da atividade de acordo com o DUA
texto_final = f"""==================================================
ATIVIDADE ESCOLAR ADAPTADA (DIRETRIZES DUA)
Nome do Aluno: ____________________________________
Data: ___/___/_____
Perfil de Inclusão: {perfil}
Tema da Aula: {tema}
==================================================

"""

if perfil == "TDAH":
    texto_final += f"""ESTUDO DO DIA: {tema.upper()}

• OS SUMÉRIOS:
  - Eles criaram a ESCRITA CUNEIFORME.
  - Escreviam fazendo desenhos em PLACAS DE BARRO.
  - Viviam na região da Mesopotâmia.

• OS FENÍCIOS:
  - Eram excelentes NAVEGADORES e COMERCIANTES.
  - Viajavam muito de barco pelo mar para vender produtos.
  - Criaram o PRIMEIRO ALFABETO do mundo para facilitar as contas.

--------------------------------------------------
[ ESPAÇO VISUAL: Cole ou desenhe uma figura sobre o tema aqui ]
--------------------------------------------------

EXERCÍCIO DE FIXAÇÃO:
Quem inventou o primeiro alfabeto do mundo?

( A ) Os Sumérios
( B ) Os Fenícios

👉 Instrução: Marque com um X a resposta correta acima.
"""
elif perfil == "Autismo (TEA)":
    texto_final += f"""CONTEÚDO DA AULA: {tema.upper()}

Os Sumérios moravam na Mesopotâmia. 
Eles inventaram a escrita cuneiforme. 
A escrita cuneiforme usava símbolos marcados em argila molhada.

Os Fenícios faziam comércio no mar. 
Eles construíam barcos fortes. 
Eles criaram um alfabeto com 22 letras.

--------------------------------------------------
[ ESPAÇO VISUAL: Cole ou desenhe uma imagem de um barco aqui ]
--------------------------------------------------

PERGUNTA DIRETA:
Qual povo criou o alfabeto para usar no comércio?

( A ) Os Fenícios
( B ) Os Sumérios
"""
else: # Deficiência Intelectual
    texto_final += f"""VAMOS APRENDER HOJE: {tema.upper()}

• SUMÉRIOS = Criaram as primeiras letras em plaquinhas de barro.
• FENÍCIOS = Criaram o alfabeto e viajavam de barco pelo mar.

--------------------------------------------------
[ ESPAÇO VISUAL: Espaço reservado para figuras e apoio concreto ]
--------------------------------------------------

ATIVIDADE LÚDICA:
Quem viajava de barco pelo mar para fazer comércio?

( A ) Os Fenícios
( B ) Os Sumérios
"""

st.markdown("---")
st.subheader("📋 Atividade Adaptada Gerada:")

# Mostra o texto estruturado na tela de forma limpa
st.text_area("Texto completo para copiar se preferir:", value=texto_final, height=350)

# Botão nativo para baixar o arquivo que abre direto no Word
st.download_button(
    label="📥 Baixar Atividade para o Word (.txt)",
    data=texto_final,
    file_name=f"Atividade_Adaptada_{perfil}.txt",
    mime="text/plain"
)
