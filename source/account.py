
class account:
    def __init__(self, name, pwd, wif, asset):
        self.name = name
        self.pwd = pwd
        self.wif = wif
        self.asset = asset

accounts = {
    "tunisie": account("bc-tunisie", "P5JwGHkFCbJqv2gqEnu4TSgmrSEqgNV63HZ9E6yPxHHBb", "5JK7dyfMt4sz6QHYUCeAcBMVuPvTudtqS294HoqFbx8UQTWN5kt", "TESTTND"),
    "maroc": account("bc-maroc", "P5Ji8wv44mLF27pC6VnZgTJB8Cy4uGmCvsWWDS3Xe9K7V", "5JxmEAcPuRsqmKqJtVTmnxDVm5gMMcpZodEg4FDFT3JXZtzAvV6", "TESTMAD"),
    "mauritanie": account("bc-mauritanie", "P5K3U1JGBMafmLd72nFHLjmDZqebYK4NiUcNy9xAz2U7Q", "5J2nbZXpNDJ5WjSh3zztUx428LDrvBeS65ReFrZ7poXz6LRtzM8", "TESTMRU"),
    "test2017": account("test2017", "P5KHthsex8FJtWb7MXRqif9vZWmZA2YkMZCNn11thKoq7", "5KWUzPCHAH9nozGh6GMJn1ojjC8Xz5wsfHnQXJ8hGtJFLz1cm6H", "TESTTND"),
    "telecom": account("maroc-telecom", "P5KVVNcEBtGwsMAD5zscmufDj4TpisnYNCPdtdZvKAqAZ", "5Jz46Rgwn9RhUoFBL6xs2XqX5P7vg83TjYsU69TT9ShD6fKS43B", "TESTMAD")
}