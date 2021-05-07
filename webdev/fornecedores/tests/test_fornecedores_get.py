import pytest
from pytest_django.asserts import assertContains
from django.urls import reverse
from django.contrib.auth.models import User
from webdev.fornecedores.models import Fornecedor, Fornecimento, Email, Telefone, Local, DadosBancarios

# Meus Fornecedores
@pytest.fixture
def resposta(client, db):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_meus_fornecedores_status_code(resposta):
    assert resposta.status_code == 200

def test_btn_novo_fornecedor_presente(resposta):
    assertContains(resposta, f'''<a href="{reverse('fornecedores:novo_fornecedor')}"''')

def test_meus_fornecedores_nao_autenticado_status_code(client, db):
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    assert resp.status_code == 302

@pytest.fixture
def lista_de_fornecedores(db):
    return [
        Fornecedor.objects.create(nome='Zé Comédia'),
        Fornecedor.objects.create(nome='Catateco'),
    ]

@pytest.fixture
def resposta_com_fornecedores(client, lista_de_fornecedores):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_meus_fornecedores_presentes(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(resposta_com_fornecedores, fornecedor.nome)

def test_btn_visualizar_fornecedor_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(resposta_com_fornecedores, f'<a href="#fornecedor{fornecedor.id}"')

def test_btn_editar_fornecedor_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:editar_fornecedor', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_deletar_fornecedor_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<form action="{reverse('fornecedores:deletar_fornecedor', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_novo_fornecimento_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:novo_fornecimento', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_novo_email_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:novo_email', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_novo_telefone_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:novo_telefone', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_novo_local_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:novo_local', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

def test_btn_novos_dados_bancarios_presente(resposta_com_fornecedores, lista_de_fornecedores):
    for fornecedor in lista_de_fornecedores:
        assertContains(
            resposta_com_fornecedores,
            f'''<a href="{reverse('fornecedores:novos_dados_bancarios', kwargs={'fornecedor_id': fornecedor.id})}"'''
        )

# Fornecimento
@pytest.fixture
def lista_de_fornecimentos(lista_de_fornecedores):
    fornecimentos = []
    for fornecedor in lista_de_fornecedores:
        novo_fornecimento = Fornecimento.objects.create(nome=f'fornecimento{fornecedor.id}', qualidade=fornecedor.id)
        fornecedor.fornecimento.add(novo_fornecimento)
        fornecimentos.append(novo_fornecimento)

    return fornecimentos

@pytest.fixture
def resposta_com_fornecimentos(client, lista_de_fornecedores, lista_de_fornecimentos):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_btn_editar_fornecimento_presente(resposta_com_fornecimentos, lista_de_fornecimentos):
    for fornecimento in lista_de_fornecimentos:
        assertContains(
            resposta_com_fornecimentos,
            f'''<a href="{reverse('fornecedores:editar_fornecimento', kwargs={'fornecimento_id': fornecimento.id})}"'''
        )

def test_btn_deletar_fornecimento_presente(resposta_com_fornecimentos, lista_de_fornecimentos):
    for fornecimento in lista_de_fornecimentos:
        assertContains(
            resposta_com_fornecimentos,
            f'''<form action="{reverse('fornecedores:deletar_fornecimento', kwargs={'fornecimento_id': fornecimento.id})}"'''
        )

# Emails
@pytest.fixture
def lista_de_emails(lista_de_fornecedores):
    emails = []
    for fornecedor in lista_de_fornecedores:
        novo_email = Email.objects.create(email=f'fornecedor{fornecedor.id}@email.com')
        fornecedor.emails.add(novo_email)
        emails.append(novo_email)
    return emails

@pytest.fixture
def resposta_com_emails(client, lista_de_fornecedores, lista_de_emails):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_btn_editar_email_presente(resposta_com_emails, lista_de_emails):
    for email in lista_de_emails:
        assertContains(
            resposta_com_emails,
            f'''<a href="{reverse('fornecedores:editar_email', kwargs={'email_id': email.id})}"'''
        )

def test_btn_deletar_email_presente(resposta_com_emails, lista_de_emails):
    for email in lista_de_emails:
        assertContains(
            resposta_com_emails,
            f'''<form action="{reverse('fornecedores:deletar_email', kwargs={'email_id': email.id})}"'''
        )

# Telefones
@pytest.fixture
def lista_de_telefones(lista_de_fornecedores):
    telefones = []
    for fornecedor in lista_de_fornecedores:
        novo_telefone = Telefone.objects.create(telefone=f'11 {fornecedor.id}')
        fornecedor.telefones.add(novo_telefone)
        telefones.append(novo_telefone)
    return telefones

@pytest.fixture
def resposta_com_telefones(client, lista_de_fornecedores, lista_de_telefones):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_btn_editar_telefone_presente(resposta_com_telefones, lista_de_telefones):
    for telefone in lista_de_telefones:
        assertContains(
            resposta_com_telefones,
            f'''<a href="{reverse('fornecedores:editar_telefone', kwargs={'telefone_id': telefone.id})}"'''
        )

def test_btn_deletar_telefone_presente(resposta_com_telefones, lista_de_telefones):
    for telefone in lista_de_telefones:
        assertContains(
            resposta_com_telefones,
            f'''<form action="{reverse('fornecedores:deletar_telefone', kwargs={'telefone_id': telefone.id})}"'''
        )

# Localisações
@pytest.fixture
def lista_de_locais(lista_de_fornecedores):
    locais = []
    for fornecedor in lista_de_fornecedores:
        novo_local = Local.objects.create(pais='Brasil')
        fornecedor.localizacoes.add(novo_local)
        locais.append(novo_local)
    return locais

@pytest.fixture
def resposta_com_locais(client, lista_de_fornecedores, lista_de_locais):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_btn_editar_locais_presente(resposta_com_locais, lista_de_locais):
    for local in lista_de_locais:
        assertContains(
            resposta_com_locais,
            f'''<a href="{reverse('fornecedores:editar_local', kwargs={'local_id': local.id})}"'''
        )

def test_btn_deletar_local_presente(resposta_com_locais, lista_de_locais):
    for local in lista_de_locais:
        assertContains(
            resposta_com_locais,
            f'''<form action="{reverse('fornecedores:deletar_local', kwargs={'local_id': local.id})}"'''
        )


# Dados Bancários 
@pytest.fixture
def lista_de_dados_bancarios(lista_de_fornecedores):
    dados_bancarios = []
    for fornecedor in lista_de_fornecedores:
        novos_dados_bancarios = DadosBancarios.objects.create(
            tipo_de_transacao='px',
            numero='11944647420'
        )
        fornecedor.dados_bancarios.add(novos_dados_bancarios)
        dados_bancarios.append(novos_dados_bancarios)
    return dados_bancarios

@pytest.fixture
def resposta_com_dados_bancarios(client, lista_de_fornecedores, lista_de_dados_bancarios):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:meus_fornecedores'))
    return resp

def test_btn_editar_dados_bancarios(resposta_com_dados_bancarios, lista_de_dados_bancarios):
    for dados_bancarios in lista_de_dados_bancarios:
        assertContains(
            resposta_com_dados_bancarios,
            f'''<a href="{reverse('fornecedores:editar_dados_bancarios', kwargs={'dados_bancarios_id': dados_bancarios.id})}"'''
        )

def test_btn_deletar_dados_bancarios(resposta_com_dados_bancarios, lista_de_dados_bancarios):
    for dados_bancarios in lista_de_dados_bancarios:
        assertContains(
            resposta_com_dados_bancarios,
            f'''<form action="{reverse('fornecedores:deletar_dados_bancarios', kwargs={"dados_bancarios_id":dados_bancarios.id}) }"'''
        )


# Novo Fornecedor
@pytest.fixture
def resposta_novo_fornecedor(client, db):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novo_fornecedor'))
    return resp

def test_novo_fornecedor_status_code(resposta_novo_fornecedor):
    assert resposta_novo_fornecedor.status_code == 200

def test_novo_fornecedor_nao_autenticado_status_code(client, db):
    resp = client.get(reverse('fornecedores:novo_fornecedor'))
    assert resp.status_code == 302


# Novo Fornecimento
@pytest.fixture
def criar_fornecedor(db):
    return Fornecedor.objects.create(nome='Zé Comédia')

@pytest.fixture
def resposta_com_fornecedor(client, criar_fornecedor):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novo_fornecimento', kwargs={'fornecedor_id':criar_fornecedor.id}))
    return resp

def test_novo_fornecimento_status_code(resposta_com_fornecedor):
    assert resposta_com_fornecedor.status_code == 200

def test_novo_fornecimento_nao_autenticado_status_code(client, criar_fornecedor):
    resp = client.get(reverse('fornecedores:novo_fornecimento', kwargs={'fornecedor_id':criar_fornecedor.id}))
    assert resp.status_code == 302


# Novo Email
@pytest.fixture
def resposta_com_fornecedor(client, criar_fornecedor):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novo_email', kwargs={'fornecedor_id':criar_fornecedor.id}))
    return resp

def test_novo_email_status_code(resposta_com_fornecedor):
    assert resposta_com_fornecedor.status_code == 200

def test_novo_email_nao_autenticado_status_code(client, criar_fornecedor):
    resp = client.get(reverse('fornecedores:novo_email', kwargs={'fornecedor_id':criar_fornecedor.id}))
    assert resp.status_code == 302


# Novo Telefone
@pytest.fixture
def resposta_com_fornecedor(client, criar_fornecedor):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novo_telefone', kwargs={'fornecedor_id':criar_fornecedor.id}))
    return resp

def test_novo_telefone_status_code(resposta_com_fornecedor):
    assert resposta_com_fornecedor.status_code == 200

def test_novo_telefone_nao_autenticado_status_code(client, criar_fornecedor):
    resp = client.get(reverse('fornecedores:novo_telefone', kwargs={'fornecedor_id':criar_fornecedor.id}))
    assert resp.status_code == 302


# Nova Localização
@pytest.fixture
def resposta_com_fornecedor(client, criar_fornecedor):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novo_local', kwargs={'fornecedor_id':criar_fornecedor.id}))
    return resp

def test_novo_telefone_status_code(resposta_com_fornecedor):
    assert resposta_com_fornecedor.status_code == 200

def test_novo_telefone_nao_autenticado_status_code(client, criar_fornecedor):
    resp = client.get(reverse('fornecedores:novo_local', kwargs={'fornecedor_id':criar_fornecedor.id}))
    assert resp.status_code == 302


# Novos Dados Bancários
@pytest.fixture
def resposta_com_fornecedor(client, criar_fornecedor):
    usr = User.objects.create_user(username='TestUser', password='MinhaSenha123')
    client.login(username='TestUser', password='MinhaSenha123')
    resp = client.get(reverse('fornecedores:novos_dados_bancarios', kwargs={'fornecedor_id':criar_fornecedor.id}))
    return resp

def test_novos_dados_bancarios_status_code(resposta_com_fornecedor):
    assert resposta_com_fornecedor.status_code == 200

def test_novos_dados_bancarios_nao_autenticado_status_code(client, criar_fornecedor):
    resp = client.get(reverse('fornecedores:novos_dados_bancarios', kwargs={'fornecedor_id':criar_fornecedor.id}))
    assert resp.status_code == 302

