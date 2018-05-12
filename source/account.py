
class account:
    def __init__(self, name, pwd, wif, asset):
        self.name = name
        self.pwd = pwd
        self.wif = wif
        self.asset = asset

accounts = {
    "tunisie": account("bc-tunisie", "P5JwGHkFCbJqv2gqEnu4TSgmrSEqgNV63HZ9E6yPxHHBb", "5JK7dyfMt4sz6QHYUCeAcBMVuPvTudtqS294HoqFbx8UQTWN5kt", "TESTTND"),
    "maroc": account("bc-maroc", "P5Ji8wv44mLF27pC6VnZgTJB8Cy4uGmCvsWWDS3Xe9K7V", "5JxmEAcPuRsqmKqJtVTmnxDVm5gMMcpZodEg4FDFT3JXZtzAvV6", "TESTMAD"),
    "mauritanie": account("bc-mauritanie", "P5K3U1JGBMafmLd72nFHLjmDZqebYK4NiUcNy9xAz2U7Q", "5J2nbZXpNDJ5WjSh3zztUx428LDrvBeS65ReFrZ7poXz6LRtzM8", "TESTMRU")
}