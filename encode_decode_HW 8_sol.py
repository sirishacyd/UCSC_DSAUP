import secrets
import string
class Codec:
    d1,d2=defaultdict(),defaultdict()
    def random_number(self):
        return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase +string.digits)for i in range(6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.d1:
            return "http://tinyurl.com/"+self.d1[longUrl]
        else:
            rnd=self.random_number()
            if rnd in self.d2:
                return self.encode(longUrl)
            self.d1[longUrl]=rnd
            self.d2[rnd]=longUrl
            return "http://tinyurl.com/"+self.d1[longUrl]
            
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s=shortUrl.split('http://tinyurl.com/')[1]
        return self.d2[s]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))