from django import forms


class AktForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shapka'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}),
                                                initial='заместитель Министра природных ресурсов\n'
                                                        'Свердловской области - \n'
                                                        'директор департамента лесного хозяйства\n')
        self.fields['bugor'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                               initial='Куряков А.В.')
        self.fields['dolgnost'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                                  initial='заместитель Министра природных ресурсов\n'
                                                          'Свердловской области - \n'
                                                          'директор департамента лесного хозяйства\n')

        self.fields['city'] = forms.CharField(max_length=255,
                                              widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              label='Город', initial='г.Ирбит')

        self.fields['fio1'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              label='ФИО первого члена комиссии',
                                              initial='Вепрев А.И.')
        self.fields['dt1'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                             label='Должность первого члена комиссии',
                                             initial='участковый лесничий Ницинского учаскового '
                                                     'лесничества ГКУ СО «Ирбитское лесничество»')

        self.fields['fio2'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              label='ФИО второго члена комиссии',
                                              initial='Перетягин С.В.')
        self.fields['dt2'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                             label='Должность второго члена комиссии',
                                             initial='индивидуальный предприниматель '
                                                     'ИП Перетягин С.В.')

        self.fields['fio3'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              label='ФИО третьего члена комиссии',
                                              initial='Сенаторов В.А.')
        self.fields['dt3'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                             label='Должность третьего члена комиссии',
                                             initial='генеральный директор '
                                                     'ООО «Уральская лесоустроительная экспедиция»')

        self.fields['fio4'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              label='ФИО четвертого члена комиссии', )
        self.fields['dt4'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                             label='Должность четвертого члена комиссии', )

        self.fields['target'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                                label='провели натурное обследование лесного участка, в целях:',
                                                initial='внесения данных натурного обследования '
                                                        'в государственный лесной реестр')
        self.fields['region'] = forms.CharField(max_length=255,
                                                widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                                label='Субъект Российской Федерации',
                                                initial='Свердловская область')
        self.fields['district'] = forms.CharField(max_length=255,
                                                  widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                                  label='Муниципальный район',
                                                  initial='Ирбитский')
        self.fields['lesn'] = forms.CharField(max_length=255, label='Лесничество',
                                              widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                              initial='ГКУ СО "Ирбитское лесничество"')
        self.fields['uch_lesn'] = forms.CharField(max_length=255, label='Участковое лесничетво',
                                                  widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                                  initial='Ницинское участковое лесничество')
        self.fields['uch'] = forms.CharField(max_length=255, label='Участок',
                                             widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                             initial='Курьинский участок')
        self.fields['ozz'] = forms.CharField(max_length=255,
                                             label='Участок имеет/не имеет особо защитное значение',
                                             widget=forms.Textarea(attrs={'class': 'form-input-1st'}),
                                             initial='не имеет')
        self.fields['lh_osob'] = forms.CharField(max_length=255,
                                                 label='Лесохозяйственные особенности участка',
                                                 widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                                 initial='предоставлен в аренду по договору ИП Перетянин С.В. '
                                                         'с целью заготовки древесины')
        self.fields['predl'] = forms.CharField(max_length=255,
                                               label='При составлении акта сделаны следующие замечания и предложения',
                                               widget=forms.Textarea(attrs={'class': 'form-input-3st'}),
                                               initial='внести данные натурного обследования в государственный '
                                                       'лесной реестр')
        self.fields['data_glr'] = forms.FileField(label='База по данным ГЛР',
                                                  widget=forms.FileInput(attrs={'class': 'button'}))
        self.fields['data_obsl'] = forms.FileField(label='База по данным натурного обследования',
                                                   widget=forms.FileInput(attrs={'class': 'button'}))
