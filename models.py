from django.db import models

# Create your models here.
class tbl_model(models.Model):
    model_no=models.IntegerField()
    model_name=models.CharField(max_length=30)
    feature=models.CharField(max_length=30)
    Photo=models.CharField(max_length=225)
    status=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_model"
class tbl_product(models.Model):
    product_id=models.CharField(max_length=30)
    model_no=models.IntegerField()
    product_name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    colour=models.CharField(max_length=30)
    price=models.IntegerField()
    stock=models.IntegerField() 
    Photo=models.CharField(max_length=225)
    status=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_product"
class tbl_account(models.Model):
    account_id=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    account_date=models.CharField(max_length=30)
    roll=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_account"
class tbl_coustomer(models.Model):
    coustomer_id=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_coustomer"
class tbl_login(models.Model):
    user_id=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_login"
class tbl_review(models.Model):
    review_id=models.CharField(max_length=30)
    coustomer_id=models.CharField(max_length=30)
    product_id=models.CharField(max_length=30)
    reviews=models.CharField(max_length=30)
    review_date=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_review"
class tbl_order(models.Model):
    order_id=models.CharField(max_length=30)
    coustomer_id=models.CharField(max_length=30)
    product_id=models.CharField(max_length=30)
    quantity=models.IntegerField()
    amount=models.IntegerField()
    order_date=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_order"
class tbl_complaint(models.Model):
    complaint_id=models.CharField(max_length=30)
    coustomer_id=models.CharField(max_length=30)
    product_id=models.CharField(max_length=30)
    complaints=models.CharField(max_length=30)
    complaint_date=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_complaint"
class tbl_payment(models.Model):
    order_id=models.CharField(max_length=30)
    payment_id=models.CharField(max_length=30)
    bank_name=models.CharField(max_length=30)
    cardtype=models.CharField(max_length=30)
    card_no=models.IntegerField()
    amount=models.IntegerField()
    payment_date=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    total=models.IntegerField(max_length=30)
    class Meta:
        db_table = "tbl_payment"
class tbl_delivery(models.Model):
    delivery_id=models.CharField(max_length=30)
    order_id=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    delivery_date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_delivery"
