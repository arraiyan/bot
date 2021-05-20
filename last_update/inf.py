
class system_vars:
    API_KEY='1831194179:AAH7m2_S8Z86SO5N3Q9Y5eHW-Q6C_mM63Ww'#this is the api key
    admin_id=['-1001355154437']#this is the admin id dont touch it
    admin_to_general=False#this boolean defines the admin mode dont touch it

    #change able vars
    forbidden_links=['https://','http://','.com','.net','.io','.xyz','.me','.health','org']#this list handels the link postings
    if_not_english="Please communicate in English or Only English allowed ."#this is a coustom massage to a non english user you can change it
    forbidden_words=['fuck','sex','fucking','sexy']#these are the forbidden words an sentenses you can add or remove more
    ################
    # THIS DICTIONARY KEEPS THE COUSTOM COMADS AND ANSWERS YOU CAN ADD EDIT AND ADD MORE BUT IT SHOULD
    # NOT BE EMTY AT ALL SECUNECE IS ={'KEY1 OR SENTENCE1':['RESULT1','RESULT2','RECULT3'.....],'KEY2 OR SENTENCE2':['RESULT1','RESULT2','RECULT3'.....]......}
    auto_response_keys={
        'buy':[
            'Send BNB,BUSD,BUSDT from your TRUST WALLET (Smart Chain) or Metamask (SmartChain) to the below smart contract address',
            '&',
            'You will receive Tokens to your Wallet from where you purchased..!\n\n0x9dc57c56fad466CAe1422ffD7404577b0e454584',
            'or visit below website \n https://safemoon.com/buy'
            ],

        'etc':[
            'key',
            ' '
            ]
    }

    #################
    interval_message_time=10 #inseconds
    interval_message=['its interval','hi']#you can add more messages
    

    interval_key=True#Dont touch this


    r1=[0,0]#dont touch it its a system variable it can harm the programme
    captcha_is_enabled=False#it cheks the captcha settings dont touch it changes can ham the programme
    new_user=[0,0]#dont touch it its a system variable it can damage the programme
    captcha_required=True


    chat_id=list()#this var will keep data of chat id;dont touch it
    chat_id_count=0#dont make any change it can hamper the programme




    