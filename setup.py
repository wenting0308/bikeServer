from setuptools import setup

setup(name="bike_server",
      version="0.1",
      description="dublin bike server",
      url="",
      author="Wen-ting, Chang",
      author_email="wen-ting.chang@ucdconnect.ie",
      licence="GPL3",
      packages=['dublin_bikes_server'],
      entry_points={
        'console_scripts':['bike_server=dublin_bikes_server.main:app.run']
        },
      )