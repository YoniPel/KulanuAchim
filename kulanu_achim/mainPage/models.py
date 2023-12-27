from django.db import models
from django.utils import timezone


# Create your models here.


class ContactInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='שם מלא')
    email = models.EmailField(verbose_name='מייל')
    phone_number = models.CharField(max_length=10, verbose_name='מספר טלפון')

    ROLE_CHOICES = [
        ('option1', 'בעל מקצוע (יועץ כלכלי, מאמן אישי, מורה פרטי, פסיכולוג, קלינאי תקשורת)'),
        ('option2', 'ארגון מקצועי'),
        ('option3', 'מוסד חינוכי (התנדבות של תלמידים)'),
        ('option4', 'נהג חלוקה'),
        ('option5', 'אחר (פרט בהודעה)'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='תפקיד')

    message = models.TextField(verbose_name='הודעה')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='נשלח בתאריך')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'מתנדב'
        verbose_name_plural = "מתנדבים"


class Volunteer(models.Model):
    name = models.CharField(max_length=100, verbose_name='שם מלא')
    email = models.EmailField(verbose_name='מייל')
    phone_number = models.CharField(max_length=10, verbose_name='מספר טלפון')

    ROLE_CHOICES = [
        ('option1', 'בעל מקצוע (יועץ כלכלי, מאמן אישי, מורה פרטי, פסיכולוג, קלינאי תקשורת)'),
        ('option2', 'ארגון מקצועי'),
        ('option3', 'מוסד חינוכי (התנדבות של תלמידים)'),
        ('option4', 'נהג חלוקה'),
        ('option5', 'אחר (פרט בהודעה)'),

    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='תפקיד')

    message = models.TextField(verbose_name='הערות')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'מתנדב קבוע'
        verbose_name_plural = "מתנדבים קבועים"


class ContactHelp(models.Model):
    # first page
    names_and_surname = models.CharField(max_length=100, verbose_name='שם הבעל והאישה ושם משפחה')
    address = models.CharField(max_length=100, verbose_name='כתובת')
    email = models.EmailField(verbose_name='מייל')
    phone_number = models.CharField(max_length=10, verbose_name='מספר טלפון')
    number_of_persons = models.TextField(verbose_name='מספר נפשות כולל פירוט (מין הילד וגיל)')

    # second page
    health_status = models.TextField(verbose_name='האם יש בעיות בריאותיות כלשהן (במידה ויש, פרט)')
    rent_status = models.TextField(max_length=500, verbose_name='האם הבית בבעלות פרטית')
    vehicle_status = models.TextField(max_length=100, verbose_name='האם יש רכב/מספר רכבים בבעלות המשפחה')
    work_status = models.TextField(max_length=500, verbose_name='האם שני ההורים עובדים')
    income_status = models.CharField(max_length=100, verbose_name='מהי ההכנסה של שני ההורים נטו (הערכה)')
    debt_status = models.TextField(verbose_name='האם המשפחה בחובות כלשהם ואם כן מהם')
    classes_status = models.TextField(verbose_name='האם הילדים (במידה ויש) בחוגים')
    baby_status = models.TextField(verbose_name='במידה ויש תינוק, האם חסר לו משהו (לפרט מה חסר)')
    clothes_status = models.TextField(verbose_name='האם חסר ביגוד (לפרט מה חסר)')
    furniture_status = models.TextField(verbose_name='האם חסר ריהוט (לפרט מה חסר)')
    air_conditioning_status = models.TextField(verbose_name='האם יש מיזוג אוויר בבית (לפרט אם חסר ואיפה)')
    appliances_and_kitchen_status = models.TextField(verbose_name='האם חסר מוצרי חשמל או מטבח בסיסיים (לפרט מה חסר)')
    cleaning_status = models.TextField(verbose_name='האם חסר מוצרי ניקיון בסיסיים (לפרט מה חסר)')
    notes = models.TextField(verbose_name='הערות', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='נשלח בתאריך')

    def __str__(self):
        return f' משפחת {self.names_and_surname}'

    class Meta:
        verbose_name = 'משפחה שזקוקה לסיוע'
        verbose_name_plural = 'משפחות שזקוקות לסיוע'
