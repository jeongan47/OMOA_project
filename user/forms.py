from django import forms
from django.core.exceptions import ValidationError
from user.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        widget = forms.TextInput(
            attrs = {"placeholder": "사용자명 (5자리 이상)"},
        )
        )
    password = forms.CharField(
        min_length=8,
        widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (8자리 이상)"},
        )
        )
    
class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        widget = forms.TextInput(
            attrs = {"placeholder": "사용자명 (5자리 이상)"},
        )
    )
    password1 = forms.CharField(
        min_length=8,
        widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (8자리 이상)"},
        )
        )
    password2 = forms.CharField(
        min_length=8,
        widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (8자리 이상)"},
        )
        )
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username = username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다")
        
        return username
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            # password2 필드에 오류를 추가
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]
        
        # 에러가 없다면, 사용자를 생성하고 로그인 처리 후 피드 페이지로 이동
        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_description = short_description,
        )
        return user