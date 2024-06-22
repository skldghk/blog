# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="사용자 이름",
        max_length=150,
        help_text="필수 항목입니다. 150자 이하. 문자, 숫자 및 @/./+/-/_ 문자만 가능합니다.",
        widget=forms.TextInput(attrs={'placeholder': '사용자 이름'})
    )
    password1 = forms.CharField(
        label="비밀번호",
        help_text=(
            "비밀번호는 다음 요구 사항을 충족해야 합니다:<br>"
            " - 비밀번호는 다른 개인 정보와 너무 유사할 수 없습니다.<br>"
            " - 비밀번호는 최소 8자 이상이어야 합니다.<br>"
            " - 비밀번호는 일반적으로 사용되는 비밀번호가 아니어야 합니다.<br>"
            " - 비밀번호는 숫자로만 구성될 수 없습니다."
        ),
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'})
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        help_text="확인을 위해 이전과 동일한 비밀번호를 입력하세요.",
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 확인'})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
