import streamlit as st

st.write('Database Usage')

conn = st.connection('pets_db', type='sql')

# pets = {'name': 'Fluffy', 'owner': 'Harold', 'species': 'dog', 'sex': 'f', 'birth': '2007-02-04', 'death': ''}

# for k in pets:
#     st.text(f'{k} = {pets[k]}')
with conn.session as s:
    
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()
st.text('Added pets to database')

pets = conn.query('select * from pet_owners')
st.dataframe(pets)

        
    