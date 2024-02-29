
with open("/Users/debasishpal/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

names_list = []
for name in names:
    names_list.append(name.strip())

with open("/Users/debasishpal/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r') as f:
    invitation_text = f.read()

# Iterate over the list of names and replace [name] in the invitation text
for n in names_list:
    customized_invitation = invitation_text.replace("[name]", n)
    with open(f"/Users/debasishpal/Downloads/Mail Merge Project Start/Output/ReadyToSend/{n}.txt", mode='w') as file:
        file.write(customized_invitation)
