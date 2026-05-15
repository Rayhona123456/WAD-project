import click
import os
from app import app

@app.cli.group()
def translate():
    """Translation commands."""
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .')
    os.system(f'pybabel init -i messages.pot -d app/translations -l {lang}')

@translate.command()
def update():
    os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .')
    os.system('pybabel update -i messages.pot -d app/translations')

@translate.command()
def compile():
    os.system('pybabel compile -d app/translations')