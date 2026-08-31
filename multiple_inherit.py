#Multiple Inheritance:

class A:
    def authenticate(self,username,pwd):
        return "authenticating user"


class B:
    def logging(self,username):
        return f'Logging {username}'


class C(A,B):
    def user_acess(self,username,pwd):
        if super().authenticate(username,pwd):
            super().logging(username)
            return True