import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from utils.log import log


class ReportManager:
    def __init__(self, output_folder=r"C:\Users\adm.joao.mendes\Documents\LOG DIARIO"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def gerar_relatorio(self, relatorios, commits, tasks, nome_arquivo=f"Relatorio_Diario {datetime.today().strftime('%d-%m-%Y')}.pdf"):
        caminho_pdf = os.path.join(self.output_folder, nome_arquivo)

        doc = SimpleDocTemplate(caminho_pdf, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Título
        story.append(Paragraph("📊 Relatório Diário - Backup Relatórios BI", styles["Title"]))
        story.append(Spacer(1, 20))

        # Data
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        story.append(Paragraph(f"🗓️ Gerado em: <b>{data_atual}</b>", styles["Normal"]))
        story.append(Spacer(1, 20))

        # Relatórios
        story.append(Paragraph("📂 Relatórios Baixados", styles["Heading2"]))
        story.append(self._montar_tabela(relatorios, ["Arquivo", "Usuário / Data"]))
        story.append(Spacer(1, 20))

        # Commits Git
        story.append(Paragraph("🌐 Alterações no GitHub", styles["Heading2"]))
        story.append(self._montar_tabela(commits, ["Arquivo", "Mensagem"]))
        story.append(Spacer(1, 20))

        # Jira
        story.append(Paragraph("📌 Tasks Jira Criadas", styles["Heading2"]))
        # converte dicionários em lista [titulo, descricao]
        tasks_formatadas = [[t.get("titulo", ""), t.get("descricao", "")] for t in tasks]
        story.append(self._montar_tabela(tasks_formatadas, ["Task", "Descrição"]))
        story.append(Spacer(1, 20))

        doc.build(story)
        log(f"[REPORT] Relatório salvo em {caminho_pdf}")
        return caminho_pdf

    def _montar_tabela(self, dados, cabecalho):
        if not dados:
            return Paragraph("Nenhum item encontrado.", getSampleStyleSheet()["Normal"])

        styles = getSampleStyleSheet()
        cell_style = ParagraphStyle(
            name="TableCell",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=0,
        )

        dados_formatados = []
        for linha in dados:
            linha_formatada = [Paragraph(str(c), cell_style) for c in linha]
            dados_formatados.append(linha_formatada)

        cabecalho_formatado = [Paragraph(c, styles["Heading5"]) for c in cabecalho]

        data = [cabecalho_formatado] + dados_formatados
        tabela = Table(data, colWidths=[250, 250])

        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4B9CD3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F9F9F9")),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ])
        tabela.setStyle(style)
        return tabela
