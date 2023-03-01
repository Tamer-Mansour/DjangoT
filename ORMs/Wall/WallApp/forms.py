from django import forms


class Login(forms.Form):
    email = forms.CharField(label="Email", max_length=255)
    password = forms.CharField(label="Password", max_length=550)


class Register(forms.Form):
    email = forms.CharField(label="Email", max_length=255)
    password = forms.CharField(label="Password", max_length=255)
    first_name = forms.CharField(label="First name", max_length=255)
    last_name = forms.CharField(label="Last name", max_length=255)


class Message(forms.Form):
    message = forms.CharField(
        label="New Message",
        widget=forms.Textarea(
            attrs={
                "class": "mdl-textfield__input",
                "rows": 3,
                "id": "new_message"
            }))


class Comment(forms.Form):
    comment = forms.CharField(
        label="Add comment:",
        widget=forms.Textarea(attrs={
            "class": "mdl-textfield__input",
            "rows": 2
        })
    )
