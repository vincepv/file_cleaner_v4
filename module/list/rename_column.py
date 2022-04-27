from config import BIRTH_NAME, CITY, COMMON_NAME, DATE_OF_BIRTH, FIRST_NAME, NUMBER, POLLING_STATION, STREET, ZIP 

rename_column = {
    "LieuDit":"lieu-dit",
    "libellé de voie": STREET,
    "LibelleVoie": STREET,
    "libelle de voie": STREET,
    "numéro de voie": NUMBER,
    "NumeroVoie": NUMBER,
    "libelle de l'ugle": CITY,
    "libellé de l'ugle": CITY,
    "code postal": ZIP,
    "code du bureau de vote": POLLING_STATION,
    "NoBureauDeVote": POLLING_STATION,
    "date de naissance": DATE_OF_BIRTH,
    "nom d'usage": COMMON_NAME,
    "NomDusage": COMMON_NAME,
    "nom de naissance": BIRTH_NAME,
    "NomdeNaissance": BIRTH_NAME,
    "prénoms": FIRST_NAME,
    
}
