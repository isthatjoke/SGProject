from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import CheckboxSelectMultiple

from hub.models import HubCategory

from post.models import Post, get_all_tags, CommentComplaint, Tags

from django.contrib.postgres.forms import SimpleArrayField


class PostCreationForm(forms.ModelForm):
    content = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget(config_name='default'))
    # tags = SimpleArrayField(forms.IntegerField)
    CHOICES = tuple((x.id, x.tag) for x in Tags.objects.all())
    # field2 = forms.MultipleChoiceField(choices=CHOICES, widget=Select2MultipleWidget)
    field2 = forms.MultipleChoiceField(choices=CHOICES, label = "Выбор тегов", widget=forms.SelectMultiple())

    tags_str = forms.CharField(
        label='Тэги поста:',
        max_length=200,
        required=False,
        # widget=forms.TextInput(
        #     attrs={'size': 67,
        #            'placeholder': 'Тэги не заданы. Выберите из списка!',}

        )

    class Meta:
        model = Post
        exclude = ('moderated', 'moderated_at', 'moderate_desc')
        fields = ('name', 'hub_category', 'tags_str', 'field2', 'status', 'user', 'karma_count', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name in ('user', 'post_karma', 'status', 'karma_count'):
                field.widget = forms.HiddenInput()
            if field_name == 'hub_category':
                field.widget.attrs['required'] = True
            if field_name == 'tags_str':
                field.widget.attrs['id'] = 'tags_str'
                field.widget.attrs['required'] = False
                field.widget.attrs['readonly'] = True
                field.widget.attrs['placeholder'] = 'Тэги не заданы. Выберите из списка!'



class PostEditForm(forms.ModelForm):
    content = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget(config_name='default'))
    CHOICES = tuple((x.id, x.tag) for x in Tags.objects.all())
    field2 = forms.MultipleChoiceField(choices=CHOICES, label="Выбор тегов", widget=forms.SelectMultiple())

    tags_str = forms.CharField(
        label='Тэги поста:',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={'size': 67,
                   'placeholder': 'Тэги не заданы. Выберите из списка!',}

        )
    )

    class Meta:
        model = Post
        exclude = ('tags', 'moderated', 'moderated_at', 'moderate_desc')
        fields = ('name', 'hub_category', 'tags_str', 'field2', 'status', 'user', 'karma_count', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name in ('user', 'post_karma', 'status', 'karma_count'):
                field.widget = forms.HiddenInput()
            if field_name == 'hub_category':
                field.widget.attrs['required'] = True
            if field_name == 'tags_str':
                field.widget.attrs['id'] = 'tags_str'
                field.widget.attrs['required'] = False
                field.widget.attrs['readonly'] = True
                field.widget.attrs['placeholder'] = 'Тэги не заданы. Выберите из списка!'


class PostModeratorEditForm(forms.ModelForm):
    STATUS_PUBLISHED = 'published'
    STATUS_ON_MODERATE = 'on_moderate'
    STATUS_NEED_REVIEW = 'need_review'
    STATUS_MODERATE_FALSE = 'moderate_false'

    STATUSES = (
        (STATUS_PUBLISHED, 'модерация подтверждена'),
        (STATUS_ON_MODERATE, 'на модерации'),
        (STATUS_NEED_REVIEW, 'необходимы исправления'),
        (STATUS_MODERATE_FALSE, 'модерация не пройдена'),
    )

    content = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget(config_name='default'))
    status = forms.ChoiceField(choices=STATUSES, label='Статус', initial=STATUS_ON_MODERATE)
    category = forms.CharField(max_length=50, label='Подкатегория')
    tags_str = forms.CharField(
        label='Тэги поста:',
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={'size': 67}
        )
    )

    class Meta:
        model = Post
        exclude = ('tags', 'moderated', 'moderated_at',)
        fields = ('name', 'category', 'tags_str', 'status', 'user', 'moderate_desc', 'karma_count', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name in ('post_karma', 'karma_count', 'user', 'hub_category'):
                field.widget = forms.HiddenInput()
            if field_name in ('tags_str', 'content', 'category', 'name'):
                field.widget.attrs['readonly'] = True
            if field_name == 'tags_str':
                field.widget.attrs['id'] = 'tags_str'
                field.widget.attrs['required'] = False
                field.widget.attrs['readonly'] = True

        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['category'].initial = instance.hub_category.name


class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )


class CreateCommentComplaintForm(forms.ModelForm):
    class Meta:
        model = CommentComplaint
        exclude = ('is_satisfied', 'created_at', 'updated_at',)
        fields = ('comment', 'user', 'complaint_type', 'complaint_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'user':
                field.widget = forms.HiddenInput()
            elif field_name == 'comment':
                field.widget.attrs['readonly'] = True
            elif field_name == 'complaint_text':
                field.widget = forms.Textarea()
