
SOLICITACOES = (('Manutenção', 'Manutenção'), ('Instalação', 'Instalação'))

TURNO = (('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno'))

SERVICOS = [
    ('Elétrico', (
            ('Gerador', 'Gerador'),
            ('Ponto de Força', 'Ponto de Força'),
            ('Ponto de iluminação', 'Ponto de iluminação'),
        )
    ),
    ('Hidráulico', (
            ('Falta de água', 'Falta de água'),
            ('Limpeza de Reservatório', 'Limpeza de Reservatório'),
            ('Reparo de Peças', 'Reparo de Peças'),
            ('Vazamento', 'Vazamento'),
            ('Desobstrução', 'Desobstrução')
        )
    ),
    ('Jardinagem e Controle de Pragas', (
            ('Plantio', 'Plantio'),
            ('Roçagem', 'Roçagem'),
            ('Controle de Pragas', 'Controle de Pragas'),
            ('Sanitização', 'Sanitização'),
        )
    ),
    ('Refrigeração', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('Refrigeração', (
            ('Split', 'Split'),
            ('Central', 'Central'),
        )
    ),
    ('Carpintaria e Marcenaria', (
            ('Infiltração Teto', 'Infiltração Teto'),
            ('Limpeza Teto', 'Limpeza Teto'),
            ('Instalação de Calhas', 'Instalação de Calhas'),
            ('Fabricação/Instalação de Móveis', 'Fabricação/Instalação de Móveis'),
            ('Instalação/Reparação de Portas e Fechaduras', 'Instalação/Reparação de Portas e Fechaduras'),
        )
    ),
    ('Serviços Gerais', (
            ('Pintura', 'Pintura'),
            ('Reparo de Gesso', 'Reparo de Gesso'),
            ('Serviço em alvenaria/Cerâmimca', 'Serviço em alvenaria/Cerâmimca'),
            ('Reformas Gerais', 'Reformas Gerais'),
        )
    ),
    ('Outros', 'Outros'),
]