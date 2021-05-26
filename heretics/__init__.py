import asyncio 
from bevy import Context 
from asyncio import get_event_loop 
from dippy.core import CacheManager, EventDispatch, Intents 
from dippy.core.api.api import DiscordAPI 
import logging, json
import os, requests
apib = "https://discord.com/api/v9/"
import multiprocessing

class Client():
    def __init__(self):
        self.loop = get_event_loop()
        self.op = False
        self.ev = {"on_message": "MESSAGE_CREATE", "on_ready": "READY"}
        self.context = Context()
        self.context.add(self.loop) 
        self.events = self.context.create(EventDispatch)
        self.context.add(self.events) 
        self.cache = self.context.create(CacheManager)
        self.context.add(self.cache)
        self.rate = 0
        multiprocessing.Process(target=self.ratelim)
    async def send(self, endpt, data):
        resp = await self.api.session.get("{apib}/{endpt}")
        json = await resp.json()
    async def check(self):
        resp = await selfapi.session.get("{apib}/users/@me")
        r = await resp.json()
        return r
    def ratelim(self): 
        while True:
            time.sleep(60)
            self.rate = 0
    def run(self):
        self.loop.run_until_complete(self.start())
    def login(self, token):
        #headers = {"Authorization": f"Bot {token}"}
        r = self.check()
        try:
            r["message"]
        except:
            self.op = True
            self.token = token
        if not self.op == True:
            raise Exception("Token Incorrect")
        else:
            self.run()
    async def start(self):
        self.api = self.context.create( DiscordAPI, self.token,     intents=Intents.ALL )
        self.context.add(self.api)
        await self.api.connect()
    def event(self, cors):
        temp = False
        try:
            self.ev[cors.__name__]
            temp = True
        except:
            pass
        if temp == False:
            raise Exception(f"{cors.__name__} is not a function")
        self.events.on(self.ev[cors.__name__], cors)
        
