from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from post.models import Post


class PostCreationForm(forms.ModelForm):
    content = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Post
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name in ('user_id', 'post_karma', 'status'):
                field.widget = forms.HiddenInput()
            if field_name == 'hub_category':
                field.widget.attrs['required'] = True


class PostEditForm(forms.ModelForm):
    content = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Post
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name in ('user_id', 'post_karma', 'status'):
                field.widget = forms.HiddenInput()
            if field_name == 'hub_category':
                field.widget.attrs['required'] = True


class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )
