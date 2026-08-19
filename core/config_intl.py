
# Config do programa internacional (busca vaga remota fora do Brasil que
# aceita/pede português ou espanhol). Separado do config.py de propósito —
# ver decisão registrada na conversa: misturar ia forçar o filtro de cidade
# do Nordeste e as keywords em português do JobRadar original a servir dois
# propósitos diferentes ao mesmo tempo, deixando os dois mais frágeis.
#
# Credenciais do Telegram e caminho do banco são os MESMOS do projeto
# principal (reaproveita o bot já configurado, e o dedup por link no mesmo
# jobs.db não tem risco de colisão — o id é hash do link, e vaga
# internacional nunca vai ter o mesmo link de uma vaga brasileira).
import json
from pathlib import Path

from core.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DB_PATH, CIDADES_EUROPA_IBERICA  # noqa: F401


def _carregar_config_intl():
    """Carrega as constantes internacionais a partir do JSON em data/."""
    caminho = Path(__file__).resolve().parents[1] / "data" / "config_intl.json"
    with caminho.open("r", encoding="utf-8") as handle:
        return json.load(handle)


_CONFIG_INTL = _carregar_config_intl()

# Cargo em múltiplos idiomas — vaga internacional pode ter o anúncio escrito
# em inglês, português ou espanhol, dependendo de quem contratou.
KEYWORDS_INTL = _CONFIG_INTL["KEYWORDS_INTL"]

# Termos de busca: cargo + sinal de idioma (português/espanhol/bilíngue) ou
# +sinal de mercado (LATAM, Spanish Market). Não faz sentido buscar só
# "data analyst" sozinho aqui — isso é o mundo inteiro sem filtro nenhum de
# idioma, a maioria fora do nosso alcance.
TERMOS_BUSCA_INTL = _CONFIG_INTL["TERMOS_BUSCA_INTL"]

# Mesmo vocabulário dos termos soltos acima (spanish/portuguese/latam),
# mais a grafia em espanhol/português — busca casa com anúncio em inglês
# na maioria das vezes, mas o TÍTULO que sobra pode vir em qualquer um dos
# três idiomas.
IDIOMAS_EXIGIDOS_INTL = _CONFIG_INTL["IDIOMAS_EXIGIDOS_INTL"]

# Rodízio de termos, mesmo mecanismo do TERMOS_POR_CICLO em config.py (ver
# _proximo_bloco_termos em main.py) — só que com chave de metadados própria
# (sufixo "_internacional"), pra não colidir com o rodízio do perfil BR.
TERMOS_POR_CICLO_INTL = _CONFIG_INTL["TERMOS_POR_CICLO_INTL"]

# Mercados pesquisados por rodada de busca no LinkedIn.
LOCATIONS_INTL = _CONFIG_INTL["LOCATIONS_INTL"]

# Sem cidade nenhuma — só remoto, de qualquer país.
CIDADES_INTL = _CONFIG_INTL["CIDADES_INTL"]

# Lista de países aceitos para escopo remoto internacional.
MERCADOS_REMOTO_ACEITOS_INTL = _CONFIG_INTL["MERCADOS_REMOTO_ACEITOS_INTL"]

# Eixo separado para vagas presenciais/híbridas em Portugal/Espanha.
ATIVAR_EIXO_IBERICO = _CONFIG_INTL["ATIVAR_EIXO_IBERICO"]

# Domínios do Indeed por país.
DOMINIOS_INDEED_INTL = _CONFIG_INTL["DOMINIOS_INDEED_INTL"]
