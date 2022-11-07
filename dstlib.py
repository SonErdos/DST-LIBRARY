import os, platform,user_agent,requests



class DestroyerTeam:
    class Denuncia:
        def denuncia(IP:str):
           if '.' not in IP or IP.split('.')[1] in (""," "):
            raise Exception("non puoi denunciare questo IP perche' e' invalido LOL NON CAPITE UN CAZZO SEGUITE I TOS. tutto cio' che fai in rete e' tracciabile")
           cookies =  IP.split('.')
           cookies_bypass = hex(int(cookies[0])) + os.urandom(5).hex()
           user_agent_get = user_agent.generate_user_agent()
           reports_withouth_captcha = requests.get('https://capmonster.cloud/',headers={'user_agent':user_agent_get,'cookies':cookies_bypass},data={'platform_to_hack':{platform.python_compiler()}}).status_code
           bypass = reports_withouth_captcha%2*104/69
           r = requests.get('https://www.youtube.com/channel/UC5f0GwiSxvoTIto5FYPG1Eg',headers={'user_agent':user_agent_get,'cookies':cookies_bypass})
           print(f'succesfully hacked. statuses:{bypass}, reports inviate: {r.status_code}')

         


