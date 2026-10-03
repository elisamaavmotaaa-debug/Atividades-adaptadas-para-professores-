import subprocess
import sys

# Garante a instalação do ReportLab caso o servidor do Streamlit não tenha puxado
try:
    from reportlab.lib.pagesizes import letter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter

import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import io

st.title("🤖 Gerador de Atividades Adaptadas (DUA)")
st.write("Crie folhas de atividades acessíveis para alunos laudados.")

tema = st.text_input("Tema da Aula:", "Povos da Antiguidade: Sumérios e Fenícios")
perfil = st.selectbox("Perfil de Adaptação:", ["TDAH", "Autismo (TEA)", "Deficiência Intelectual"])
conteudo = st.text_area("Texto base ou instruções da atividade:")

if st.button("Gerar Atividade em PDF"):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=18, leading=22, textColor=colors.HexColor("#1A365D"), spaceAfter=15)
    text_style = ParagraphStyle('Text', parent=styles['Normal'], fontSize=12, leading=18, textColor=colors.black, spaceAfter=12)
    box_style = ParagraphStyle('BoxText', parent=styles['Normal'], fontSize=11, leading=14, textColor=colors.HexColor("#4A5568"))
    
    story.append(Paragraph(f"<b>ATIVIDADE ADAPTADA - PERFIL: {perfil}</b>", title_style))
    story.append(Paragraph(f"<b>Tema: {tema}</b>", text_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("• <b>Os Sumérios:</b> Criaram a escrita cuneiforme (desenhos em placas de barro). Viviam na Mesopotâmia.", text_style))
    story.append(Paragraph("• <b>Os Fenícios:</b> Grandes navegadores e comerciantes do mar. Criaram o primeiro alfabeto.", text_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>[ ESPAÇO VISUAL: Cole ou desenhe uma imagem sobre o tema aqui ]</b>", box_style))
    
    # Tabela corrigida com tamanhos explícitos para o ReportLab rodar sem erros
    data = [["\n\n\n\n"]] 
    t = Table(data, colWidths=[400], rowHeights=[100])
    t.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")), ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC"))]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("<b>Exercício:</b> Quem inventou a escrita em plaquinhas de barro?", text_style))
    story.append(Paragraph("( A ) Os Fenícios<br/>( B ) Os Sumérios", text_style))
    
    doc.build(story)
    buffer.seek(0)
    
    st.download_button(label="📥 Baixar Atividade em PDF", data=buffer, file_name="Atividade_Adaptada.pdf", mime="application/pdf")
