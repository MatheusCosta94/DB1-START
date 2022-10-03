#Importar Discord e OS
import discord
import os

#Chamar TOKEN gerado pelo Discord salvo em my_secret
my_secret = os.environ['TOKEN']
client = discord.Client(intents=discord.Intents.all())

#Informar que está logado
@client.event
async def on_ready():
    print('Estou logado como {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
#Responder ao chamado dos usuários
  if message.content.startswith('$Olá'):
    await message.channel.send(f'Olá, me chamo Moderator e irei te ajudar. A Príncipio irei te enviar as opções de informações que posso te dar, em seguida você deve responder a mensagem com a opção desejada, por exemplo $Hora.  Esse abaixo é o nosso Menu principal:{os.linesep}1- $Regras{os.linesep}2- $Dicas{os.linesep}3- $Desenvolvedor')

#Responder quais são as regras
  if message.content.startswith('$Regras'):
    await message.channel.send(f'As Regras deste servidor são: {os.linesep}1 - Seja educado(a), respeito é bom e de graça, use e abuse dele{os.linesep}2 - O servidor do discord tem disponibilidade para qualquer pessoa, indiferentemente da etnia, sexualidade, etc{os.linesep}3 - A utilização do chat de dúvidas deverá ser apenas e unicamente para sanar dúvidas{os.linesep}4 - A utilização do batepapo deverá ser apenas e unicamente para conversas entre jogadores{os.linesep}5 - É proibido ofender qualquer jogador ou administrador no discord{os.linesep}6 - Assédio é estritamente proibido{os.linesep}7 - Proibido fazer postagens racistas, homofóbicas e com qualquer conteúdo +18{os.linesep}8 - Recrutamentos devem ser divulgados SOMENTE nas salas especificas{os.linesep}9 - Evite spam, Mensagens repetidas atrapalham o chat, por favor, tenha bom senso{os.linesep}10 - Por favor, não grite. Evite o uso excessivo do CAPS LOCK{os.linesep}{os.linesep}!! ATENÇÃO !!{os.linesep}{os.linesep}Qualquer que infrigir as regras está passível de expulsão do servidor{os.linesep}{os.linesep}Para Retornar ao Menu responda a minha mensagem com $Menu ')

#Conceder Dicas ao Usuário
  if message.content.startswith('$Dicas'):
    await message.channel.send(f'Dicas de Uso:{os.linesep}1 - Ajude o próximo, gentileza gera gentileza{os.linesep}2 - Evita disponibilizar dados pessoais com outros participantes{os.linesep}3 - Relate ao administrador qualquer problema, para que possemos melhorar o servidor')


#Narrar história do Desenvolvedor do Bot
  if message.content.startswith('$Desenvolvedor'):
    await message.channel.send(f'Olá, tudo bem? vou ter contar um pouco da história de Matheus Costa. Matheus possui 28 anos de idade, é casado a 4 anos com Amanda Cecília. Matheus é natural de Natal-RN, mas mora em São Gonçalo do Amarante que é zona metropolitana de Natal. Trabalha como Analista da Qualidade Pleno no maior supermercado Potiguar, e está se preparando para todo esse momento tecnológico que o mundo está vivendo, certo de que suas vivências profissionais podem contribuir para essa evolução, pois formado em Administração e agora cursando pós graduação em Inteligência Artificial e Ciência de Dados, Ele casou o conhecimento de Negócios com Tecnologia')
client.run(my_secret)
