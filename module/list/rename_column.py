from config import BIRTH_NAME, CITY, COMMON_NAME, DATE_OF_BIRTH, FIRST_NAME, NUMBER, STREET, ZIP 

rename_column = {
    "numéro de voie": NUMBER,
    "NumeroVoie": NUMBER,
    "commune": CITY,
    "code du bureau de vote": "numero bv",
    "NoBureauDeVote": "numero bv",
    "libellé de voie": STREET,
    "LibelleVoie": STREET,
    "code postal": ZIP,
    "date de naissance": DATE_OF_BIRTH,
    "nom d'usage": COMMON_NAME,
    "NomDusage": COMMON_NAME,
    "nom de naissance": BIRTH_NAME,
    "NomdeNaissance": BIRTH_NAME,
    "prénoms": FIRST_NAME,
    "LieuDit":"lieu-dit",
}
