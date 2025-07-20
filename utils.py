from kavenegar import *
from omdbapi.movie_search import GetMovie

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('694D527046576C6D796E3657384C6350527673612F36436C6364667551422B58566E6632714F2B774A44343D')
        params = { 'sender' : '2000500666',
                'receptor': phone_number,
                'message' :f'این کد یکبار مصرف برای احراز هویت سایت نقد فیلم می باشد.\n{code}' }
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)