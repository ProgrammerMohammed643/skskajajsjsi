from telebot import *
from requests import *
from user_agent import *
from telebot.types import InlineKeyboardMarkup as Mk , 	   InlineKeyboardButton as btn 
TOKEN = "6598206012:AAHmGat1fAWSNnvMxeary5btrCZ8dWPj7x4"
bot = TeleBot(TOKEN)
key = Mk()
key.add(btn(text="✨ᴍᴏʜᴧᴍᴍᴇᴅ✨",url="t.me/KOK0KK")) 
key.add(btn(text="channel",url="t.me/Your_uncle_Muhammad")) 
@bot.message_handler(commands=['start'])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f'''*• أهلا بك عزيزي :* {tag} *.
• أرسل ما الذي تبحث عنه؟ . *'''
	bot.send_photo(message.chat.id,photo,text ,
	parse_mode="Markdown",reply_markup=key)
@bot.message_handler(func=lambda message:True)
def main(message):
	i = 1
	try:
		url = 'https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/my_pins/?q=avengers&rs=rs&eq=naruto%208K&etslf=15092&term_meta[]=avengers%7Crecentsearch%7C4&data={"options":{"article":null,"applied_filters":null,"appliedProductFilters":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"query":"'+message.text+'","query_pin_sigs":null,"redux_normalize_feed":true,"rs":"direct_navigation","scope":"pins","source_id":null,"no_fetch_context_on_resource":false},"context":{}}&_=1662617352806'
		headers = {
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'csrftoken=0e018d7a846bbb9b8fa7832662c63ed2; _b="AWbcYA0FqcRO6pt4TXz6L96G+/bXeigv/QK5RoON+UKFoKfeyCZZ/IQx+Ka7R9tJhOc="; g_state={"i_l":0}; _auth=1; _pinterest_sess=TWc9PSZoUjNlM2o4dlk2Nis0K3M5bThOOWlzcVVZQ2xKK0grQVhScjU0Vk14M0dYTEswUUMrako1YmNiYk8xaStHSHpnQ2Ezbzc1Rlg1TkZqZkM3djVqRkg2VEg3MTNGZEd4UURRZHc2Njlpam5BdmxFV1hhaW9LNzJ2TWpLdkg3K3krTDJzYXhqbndWeXltYUh5NzVQNEF0M2NQZTc4dVl5RkhDNlFkbGNBa1F0cU0rSEpHclY0dDJHRGdrRWdRdkpoeXhBK3lmMkp3MHh2Z3NJZzVkVm1WTDdJd2ZsQTB3YWI4N2h3c3hnU2tiWU9zYW5sQUJxWFBiSElyRGZTY3hWd2MrZURnSk9idnZ2cFhoUmtTTlRjWGhxTHhNVE9EaTVSQ1FMM2toQmRIYjdCSmVDSklJSFNlMVVycjJ6STdXbnNBaG5nL0xRUFVZYmhxZEtMOUJTKzNqTE9zK1ZYTDNHeEpzOWxXTmpVWkRXRHg4SDUyVkZIZEtxMzZBVnVBZjd2czBKSHp1K0QyV21rOEt3OG03MUdYcVFIVTEvci9VRW9jblplSHE2TGFQZVgrKzlvS2JJK2pRcis1S1JHbU9IYUtYSkVJaENaT05pZXNvd2krMUxNeDVkYnhtK3N0cEMwMzRlMSsrZXVQUEpZdTJtSXZsTTBxWGs1ZmtqYnBUcmJJMlEwSW55ak1mWXVtclV5bzhtTEhadGtLV21LbkVqdzFKelBZWmVlZWE4eGRVNjQ4NFNablRDUTJnb3F0ZTVkWWx1UHdjOXVJWGtwRWtsSit2dHpkMmVzeUxEOHFzdzdmS3NKVnFITDJwUjlDYnRMWWJSeURtQWZ5MloxV1c0WEp4RkQ3SWRKTm1Bc0ZYMDdUR0pubkRXUVpKRS8xNmxQNWNvYUpSb3dtNHlWencvWncrS2hkOXFBNlNsTW5Ha1lpVkdhZ2dMQmhsOUxGN2s4cmdwQUpDRmV5ODVDb0sreWtnNzdhdjZUWjBnLzJ4MlJjdXVHOVI2ZXovUm1KTTQwVmFTREJTUkVvWUF3WEx0QnhwWEtEU2NxSmpXZjNWREcxTWpTb0MrOCtiOW1JbFEvOUlUUFJCNTc4SzJkSTByOG5ieW94UWZ0OWVFR3RPUmpWRGZ2NFRYNTYzRGd5RVlZK1o3UkhVTG5xVUZ5cVlzakl6a2U0Vks1YmQ5SUpkckgvVTlTY2tqblVIU3dmUnRTdkhtL2F6SnFWUnVsMkVwZGRyUlQ5Rk9CMlNzb2VieFYxTDc2UU8vcnBZcjFMR1h5aFV2VFRSRlFrbGppczNYYVh4NXAwcG54TUx3TnpiczZhQTJOMHMxdzgyVitFPSZtUTFDTnV5UTdrNit6R0Q5VDJyS0dXZGN3R0k9; _routing_id="2446e1bc-a370-4e3c-8e3c-ec9ec536d20f"; sessionFunnelEventLogged=1; cm_sub=none','pragma': 'no-cache',
        'referer': 'https://www.pinterest.com/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()) ,
        'x-app-version': 'a332b16','x-pinterest-appstate': 'active',
        'x-pinterest-experimenthash': 'c519017d978aab61a2dc39b3ed657696bcb130c2aa27632777fcafe1dcae2bce503172a4f5554e6bf64bdce07f29915629f8bc0c126647930a83f3fe6f8d8795',
        'x-pinterest-pws-handler': 'www/search/[scope].js',
        'x-pinterest-source-url': '/search/pins/?q=avengers&rs=typed&term_meta[]=avengers%7Ctyped',
        'x-requested-with': 'XMLHttpRequest'}
		res = get(url,headers=headers).json()['resource_response']['data']['results']
		while True:
			result = res[i]['images']['orig']['url']
			bot.send_photo(message.chat.id,result);i+=1
	except:pass
bot.infinity_polling()


