from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='昵称 / 用户名',
        required=True,
        min_length=3,
        max_length=10,
        widget=forms.TelInput(attrs={'class':'form-control'}),
        error_messages={
            'required':'用户名不可以为空',
            'min_length':'长度不可以小于3个字符',
            'max_length':'长度不可以大于10个字符'
        }
    )

    password = forms.CharField(
        label='密码',
        required=True,
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入8-30位密码'}),
        error_messages={
            'required':'密码不可为空',
            'min_length':'密码不可以小于8个字符',
            'max_length':'密码不可以大于30个字符'
        }
    )
