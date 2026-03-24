import discord
import asyncio
import os
from colorama import init, Fore, Style
    print(Fore.RED + "========================================")
    print(Fore.WHITE + "      DISCORD MULTI-CHANNEL TEST        ")
    print(Fore.RED + "========================================\n")

async def iniciar():
    banner()

    # Inputs interativos
    print(Fore.RED + "[" + Fore.WHITE + "!" + Fore.RED + "]" + Fore.WHITE + " Configuração:")
    token = input(Fore.WHITE + "    TOKEN: " + Fore.RED).strip()
    server_id = input(Fore.WHITE + "    SERVER ID: " + Fore.RED).strip()
    
    print(Fore.RED + "\n[" + Fore.WHITE + "!" + Fore.RED + "]" + Fore.WHITE + " Conteúdo:")
    mensagem = input(Fore.WHITE + "    MENSAGEM: " + Fore.RED)

    intents = discord.Intents.default()
    intents.guilds = True
    intents.messages = True
    intents.message_content = True

    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f"\n{Fore.WHITE}[*] Logado como: {Fore.RED}{bot.user}")
        
        try:
            guild = bot.get_guild(int(server_id))
            if guild:
                print(f"{Fore.WHITE}[*] Servidor Alvo: {Fore.RED}{guild.name}\n")
                
                for channel in guild.text_channels:
                    try:
                        await channel.send(mensagem)
                        print(f"{Fore.RED}[+]{Fore.WHITE} Enviado: #{channel.name}")
                        await asyncio.sleep(0.4) # Delay para evitar bloqueio da API
                    except:
                        print(f"{Fore.RED}[-]{Fore.WHITE} Sem permissão: #{channel.name}")
            else:
                print(f"\n{Fore.RED}[!] Erro: Servidor não encontrado.")
        except ValueError:
            print(f"\n{Fore.RED}[!] Erro: ID do servidor inválido.")
        
        print(f"\n{Fore.WHITE}[*] Processo finalizado.")
        await bot.close()

    try:
        await bot.start(token)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Falha Crítica: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(iniciar())
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Fechando ferramenta...")
