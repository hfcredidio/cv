personal = dict(
        first_name  = 'Heitor',
        middle_name = 'Fernandes',
        last_name   = 'Credidio',
        address = dict(base        = 'Andrade Furtado St., 1195, A602',
                       postal_code = '60-192072',
                       city        = 'Fortaleza',
                       state       = 'Ceará',
                       country     = 'Brazil'),
        dob         = '1988-05-10',
        nationality = 'Brazilian/Portuguese',
        telephone   = '+55 85 98610 1005',
        skype       = 'hfcredidio',
        twitter     = '@htrcrd',
        github      = 'hfcredidio',
        email       = 'hfcredidio@gmail.com',
        site        = 'http://www.credid.io',
        others      = ['Eligible to work in the EU'],
)

grad = dict(
        title        = 'Bachelor in Physics',
        start        = '2006',
        end          = '2009',
        institution  = 'Universidade Federal do Ceará',
        city         = 'Fortaleza',
        state        = 'Ceará',
        country      = 'Brazil',
        thesis_type  = 'Monograph',
        thesis_title = 'Computer Simulation of Granular Materials',
        advisor      = 'Prof. André Auto Moreira',
        description  = None,
)

master = dict(
        title        = 'Master in Physics',
        start        = '2010',
        end          = '2012',
        institution  = 'Universidade Federal do Ceará',
        city         = 'Fortaleza',
        state        = 'Ceará',
        country      = 'Brazil',
        thesis_type  = 'Dissertation',
        thesis_title = 'Statistical Patterns of Eye Movements in Visual Search',
        advisor      = 'Prof. José Soares de Andrade Jr.',
        description  = 'Strong focus on data exploration, analysis and visualization.',
)

phd = dict(
        title        = 'Doctor in Physics',
        start        = '2012',
        end          = '2016',
        institution  = 'Universidade Federal do Ceará',
        city         = 'Fortaleza',
        state        = 'Ceará',
        country      = 'Brazil',
        thesis_type  = 'Thesis',
        thesis_title = 'Schramm-Loewner Evolutions of Strongly Anisotropic Systems',
        advisor      = 'Prof. José Soares de Andrade Jr.',
        description  = 'Involved analysis of larger datasets and implementation of '
                       'optimization techniques like GPU parallelization. '
                       'In collaboration with ETH-Zürich.',
)

teach = dict(
        title        = 'Temporary Lecturer',
        start        = '01/11',
        end          = '12/12',
        institution  = 'Universidade Federal do Ceará',
        city         = 'Fortaleza',
        state        = 'Ceará',
        country      = 'Brazil',
        thesis_type  = None,
        thesis_title = None,
        advisor      = None,
        description  = 'Taught courses on introductory physics for '
                       'science and engineering freshmen for four semesters.',
)

ta = dict(
        title        = 'Teacher Assistant',
        start        = '07/13',
        end          = '12/13',
        institution  = 'Universidade Federal do Ceará',
        city         = 'Fortaleza',
        state        = 'Ceará',
        country      = 'Brazil',
        thesis_type  = None,
        thesis_title = None,
        advisor      = None,
        description  = 'Supervised laboratory classes for engineering students.'
)

pub1 = dict(
        authors  = ['HF Credidio', 'EN Teixeira', 'SDS Reis',
                    'AA Moreira', 'JS Andrade Jr'],
        citation = 'Scientific Reports 2: 920 (2012)',
        title    = 'Statistical patterns of visual search for hidden objects',
        year     = '2012',
        link     = 'goo.gl/cKhQQS',
        notes    = 'Presented in the Brazilian Physics Congress in 2011',
)

pub2 = dict(
        authors  = ['HF Credidio', 'EN Teixeira', 'SDS Reis',
                    'AA Moreira', 'JS Andrade Jr'],
        citation = 'In: Perspectives and Challenges in Statistical '
                   'Physics and Complex Systems for the Next Decade (2014)',
        title    = 'Multiplicative processes in visual cognition',
        year     = '2014',
        link     = 'db.tt/C2qzVq9X'
)

pub3 = dict(
        authors  = ['HF Credidio', 'HJ Herrmann',
                    'AA Moreira', 'JS Andrade Jr'],
        citation = 'Physical Review E 93 (4), 042124 (2016)',
        title    = 'Stochastic Loewner evolution relates anomalous '
                   'diffusion and anisotropic percolation',
        year     = '2016',
        link     = 'goo.gl/hRtp2Z',
        notes    = 'To be presented in the XXVI STATPHYS in 2016'
)

pub4 = dict(
        authors  = ['HPM Melo', 'HF Credidio', 'JS Andrade Jr'],
        citation = '(In progress)',
        title    = 'Scaling and criticality in CO2 emissions in the US '
                   '(tentative title)',
        year     = '',
        link     = '',
)

skills = dict(
        programming = [('Python', '3'), ('C', '3'), ('C++', '3'),
                       ('CUDA', '2'), ('HTML/CSS', '2'),
                       ('Javascript', '2')],
        other_programming = ['Bash', 'R', 'SQL', 'Git', 'Fortran'],
        software = [('GNU/Linux', '3'), ('OS/X', '3'), ('Windows', '2'),
                    ('')],
        languages = [('Portuguese', 'Native'), ('English', 'Fluent'),
                     ('French', 'Conversational')],
        personal = ['Good at public speaking'],
)

if __name__ == '__main__':
    cv = {}
    cv['personal'] = personal
    cv['education'] = [phd, master, grad]
    cv['experience'] = [ta, teach]
    cv['publications'] = [pub4, pub3, pub2, pub1]
    cv['skills'] = skills

    import json
    with open('cv.json', 'w') as fout:
        json.dump(cv, fout, indent=5)
