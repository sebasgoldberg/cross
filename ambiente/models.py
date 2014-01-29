# coding=utf-8

class BaseAmbiente:

  def get_base_url(self):
    return self.get_base_http()

  def get_base_http(self):
    return 'http://%s:%s'%(self.dominio,self.puerto_http)

  def get_base_https(self):
    return 'https://%s:%s'%(self.dominio,self.puerto_https)
