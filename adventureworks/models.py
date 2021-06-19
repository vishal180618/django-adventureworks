# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
"""
Authors Note:
This is not the direct output of command `python manage.py inspectdb`.
Comments generated from `inspectdb` command are removed.
Models are converted to capitalcase and Models fields are converted to snakecase.
`managed = False` is removed from Meta.
"""
from django.db import models


class HumanResourcesDepartment(models.Model):
    department_id = models.SmallIntegerField(db_column='DepartmentID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    group_name = models.CharField(db_column='GroupName', max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_Department'


class HumanResourcesEmployee(models.Model):
    business_entity = models.OneToOneField('Person', models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    national_id_number = models.CharField(db_column='NationalIDNumber', unique=True, max_length=15, db_collation='utf8mb4_general_ci')
    login_id = models.CharField(db_column='LoginID', unique=True, max_length=256, db_collation='utf8mb4_general_ci')
    organization_node = models.CharField(db_column='OrganizationNode', max_length=255, blank=True, null=True)
    organization_level = models.SmallIntegerField(db_column='OrganizationLevel', blank=True, null=True)
    job_title = models.CharField(db_column='JobTitle', max_length=50, db_collation='utf8mb4_general_ci')
    birth_date = models.DateField(db_column='BirthDate')
    marital_status = models.CharField(db_column='MaritalStatus', max_length=1, db_collation='utf8mb4_general_ci')
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='utf8mb4_general_ci')
    hire_date = models.DateField(db_column='HireDate')
    salaried_flag = models.IntegerField(db_column='SalariedFlag')
    vacation_hours = models.SmallIntegerField(db_column='VacationHours')
    sick_leave_hours = models.SmallIntegerField(db_column='SickLeaveHours')
    current_flag = models.IntegerField(db_column='CurrentFlag')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_Employee'


class HumanResourcesEmployeeDepartmentHistory(models.Model):
    business_entity = models.OneToOneField(HumanResourcesEmployee, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    department = models.ForeignKey(HumanResourcesDepartment, models.DO_NOTHING, db_column='DepartmentID')
    shift = models.ForeignKey('HumanResourcesShift', models.DO_NOTHING, db_column='ShiftID')
    start_date = models.DateField(db_column='StartDate')
    end_date = models.DateField(db_column='EndDate', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_EmployeeDepartmentHistory'
        unique_together = (('business_entity_id', 'department_id', 'shift_id', 'start_date'),)


class HumanResourcesEmployeePayHistory(models.Model):
    business_entity = models.OneToOneField(HumanResourcesEmployee, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    rate_change_date = models.DateTimeField(db_column='RateChangeDate')
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)
    pay_frequency = models.PositiveIntegerField(db_column='PayFrequency')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_EmployeePayHistory'
        unique_together = (('business_entity_id', 'rate_change_date'),)


class HumanResourcesJobCandidate(models.Model):
    job_candidate_id = models.IntegerField(db_column='JobCandidateID', primary_key=True)
    business_entity = models.ForeignKey(HumanResourcesEmployee, models.DO_NOTHING, db_column='BusinessEntityID', blank=True, null=True)
    resume = models.TextField(db_column='Resume', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_JobCandidate'


class HumanResourcesShift(models.Model):
    shift_id = models.PositiveIntegerField(db_column='ShiftID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    start_time = models.TimeField(db_column='StartTime')
    end_time = models.TimeField(db_column='EndTime')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'HumanResources_Shift'
        unique_together = (('start_time', 'end_time'),)


class PersonAddress(models.Model):
    address_id = models.IntegerField(db_column='AddressID', primary_key=True)
    address_line1 = models.CharField(db_column='AddressLine1', max_length=60, db_collation='utf8mb4_general_ci')
    address_line2 = models.CharField(db_column='AddressLine2', max_length=60, db_collation='utf8mb4_general_ci', blank=True, null=True)
    city = models.CharField(db_column='City', max_length=30, db_collation='utf8mb4_general_ci')
    state_province = models.ForeignKey('PersonStateProvince', models.DO_NOTHING, db_column='StateProvinceID')
    postal_code = models.CharField(db_column='PostalCode', max_length=15, db_collation='utf8mb4_general_ci')
    spatial_location = models.TextField(db_column='SpatialLocation', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_Address'
        unique_together = (('address_line1', 'address_line2', 'city', 'state_province_id', 'postal_code'),)


class PersonAddressType(models.Model):
    address_type_id = models.IntegerField(db_column='AddressTypeID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_AddressType'


class PersonBusinessEntity(models.Model):
    business_entity_id = models.IntegerField(db_column='BusinessEntityID', primary_key=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_BusinessEntity'


class PersonBusinessEntityAddress(models.Model):
    business_entity = models.OneToOneField(PersonBusinessEntity, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    address = models.ForeignKey(PersonAddress, models.DO_NOTHING, db_column='AddressID')
    address_type = models.ForeignKey(PersonAddressType, models.DO_NOTHING, db_column='AddressTypeID')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_BusinessEntityAddress'
        unique_together = (('business_entity_id', 'address_id', 'address_type_id'),)


class PersonBusinessEntityContact(models.Model):
    business_entity = models.OneToOneField(PersonBusinessEntity, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='PersonID')
    contact_type = models.ForeignKey('PersonContactType', models.DO_NOTHING, db_column='ContactTypeID')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_BusinessEntityContact'
        unique_together = (('business_entity_id', 'person_id', 'contact_type_id'),)


class PersonContactType(models.Model):
    contact_type_id = models.IntegerField(db_column='ContactTypeID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_ContactType'


class PersonCountryRegion(models.Model):
    country_region_code = models.CharField(db_column='CountryRegionCode', primary_key=True, max_length=3, db_collation='utf8mb4_general_ci')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_CountryRegion'


class PersonEmailAddress(models.Model):
    business_entity = models.OneToOneField('Person', models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    email_address_id = models.IntegerField(db_column='EmailAddressID')
    email_address = models.CharField(db_column='EmailAddress', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_EmailAddress'
        unique_together = (('business_entity_id', 'email_address_id'),)


class PersonPassword(models.Model):
    business_entity = models.OneToOneField('Person', models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    password_hash = models.CharField(db_column='PasswordHash', max_length=128)
    password_salt = models.CharField(db_column='PasswordSalt', max_length=10)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_Password'


class Person(models.Model):
    business_entity = models.OneToOneField(PersonBusinessEntity, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    person_type = models.CharField(db_column='PersonType', max_length=2, db_collation='utf8mb4_general_ci')
    name_style = models.IntegerField(db_column='NameStyle')
    title = models.CharField(db_column='Title', max_length=8, db_collation='utf8mb4_general_ci', blank=True, null=True)
    first_name = models.CharField(db_column='FirstName', max_length=100, db_collation='utf8mb4_general_ci')
    middle_name = models.CharField(db_column='MiddleName', max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)
    last_name = models.CharField(db_column='LastName', max_length=100, db_collation='utf8mb4_general_ci')
    suffix = models.CharField(db_column='Suffix', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    email_promotion = models.IntegerField(db_column='EmailPromotion')
    additional_contact_info = models.TextField(db_column='AdditionalContactInfo', blank=True, null=True)
    demographics = models.TextField(db_column='Demographics', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_Person'


class PersonPhone(models.Model):
    business_entity = models.OneToOneField(Person, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    phone_number = models.CharField(db_column='PhoneNumber', max_length=50, db_collation='utf8mb4_general_ci')
    phone_number_type = models.ForeignKey('PersonPhoneNumberType', models.DO_NOTHING, db_column='PhoneNumberTypeID')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_PersonPhone'
        unique_together = (('business_entity_id', 'phone_number', 'phone_number_type_id'),)


class PersonPhoneNumberType(models.Model):
    phone_number_type_id = models.IntegerField(db_column='PhoneNumberTypeID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_PhoneNumberType'


class PersonStateProvince(models.Model):
    state_province_id = models.IntegerField(db_column='StateProvinceID', primary_key=True)
    state_province_code = models.CharField(db_column='StateProvinceCode', max_length=3, db_collation='utf8mb4_general_ci')
    country_region_code = models.ForeignKey(PersonCountryRegion, models.DO_NOTHING, db_column='CountryRegionCode')
    is_only_state_province_flag = models.IntegerField(db_column='IsOnlyStateProvinceFlag')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    territory = models.ForeignKey('SalesTerritory', models.DO_NOTHING, db_column='TerritoryID')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Person_StateProvince'
        unique_together = (('state_province_code', 'country_region_code'),)


class ProductionBillOfMaterials(models.Model):
    bill_of_materials_id = models.IntegerField(db_column='BillOfMaterialsID', primary_key=True)
    product_assembly = models.ForeignKey('ProductionProduct', models.DO_NOTHING, db_column='ProductAssemblyID', blank=True, null=True)
    component = models.ForeignKey('ProductionProduct', models.DO_NOTHING, db_column='ComponentID')
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    unit_measure_code = models.ForeignKey('ProductionUnitMeasure', models.DO_NOTHING, db_column='UnitMeasureCode')
    b_o_m_level = models.SmallIntegerField(db_column='BOMLevel')
    per_assembly_qty = models.DecimalField(db_column='PerAssemblyQty', max_digits=8, decimal_places=2)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_BillOfMaterials'
        unique_together = (('product_assembly_id', 'component_id', 'start_date'),)


class ProductionCulture(models.Model):
    culture_id = models.CharField(db_column='CultureID', primary_key=True, max_length=6, db_collation='utf8mb4_general_ci')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_Culture'


class ProductionDocument(models.Model):
    document_node = models.CharField(db_column='DocumentNode', primary_key=True, max_length=255)
    document_level = models.SmallIntegerField(db_column='DocumentLevel', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=50, db_collation='utf8mb4_general_ci')
    owner = models.ForeignKey(HumanResourcesEmployee, models.DO_NOTHING, db_column='Owner')
    folder_flag = models.IntegerField(db_column='FolderFlag')
    file_name = models.CharField(db_column='FileName', max_length=400, db_collation='utf8mb4_general_ci')
    file_extension = models.CharField(db_column='FileExtension', max_length=8, db_collation='utf8mb4_general_ci')
    revision = models.CharField(db_column='Revision', max_length=5, db_collation='utf8mb4_general_ci')
    change_number = models.IntegerField(db_column='ChangeNumber')
    status = models.PositiveIntegerField(db_column='Status')
    document_summary = models.TextField(db_column='DocumentSummary', db_collation='utf8mb4_general_ci', blank=True, null=True)
    document = models.TextField(db_column='Document', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_Document'
        unique_together = (('document_level', 'document_node'),)


class ProductionIllustration(models.Model):
    illustration_id = models.IntegerField(db_column='IllustrationID', primary_key=True)
    diagram = models.TextField(db_column='Diagram', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_Illustration'


class ProductionLocation(models.Model):
    location_id = models.SmallIntegerField(db_column='LocationID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    cost_rate = models.DecimalField(db_column='CostRate', max_digits=10, decimal_places=4)
    availability = models.DecimalField(db_column='Availability', max_digits=8, decimal_places=2)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_Location'


class ProductionProduct(models.Model):
    product_id = models.IntegerField(db_column='ProductID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    product_number = models.CharField(db_column='ProductNumber', unique=True, max_length=25, db_collation='utf8mb4_general_ci')
    make_flag = models.IntegerField(db_column='MakeFlag')
    finished_goods_flag = models.IntegerField(db_column='FinishedGoodsFlag')
    color = models.CharField(db_column='Color', max_length=15, db_collation='utf8mb4_general_ci', blank=True, null=True)
    safety_stock_level = models.SmallIntegerField(db_column='SafetyStockLevel')
    reorder_point = models.SmallIntegerField(db_column='ReorderPoint')
    standard_cost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=4)
    list_price = models.DecimalField(db_column='ListPrice', max_digits=19, decimal_places=4)
    size = models.CharField(db_column='Size', max_length=5, db_collation='utf8mb4_general_ci', blank=True, null=True)
    size_unit_measure_code = models.ForeignKey('ProductionUnitMeasure', models.DO_NOTHING, db_column='SizeUnitMeasureCode', blank=True, null=True)
    weight_unit_measure_code = models.ForeignKey('ProductionUnitMeasure', models.DO_NOTHING, db_column='WeightUnitMeasureCode', blank=True, null=True)
    weight = models.DecimalField(db_column='Weight', max_digits=8, decimal_places=2, blank=True, null=True)
    days_to_manufacture = models.IntegerField(db_column='DaysToManufacture')
    product_line = models.CharField(db_column='ProductLine', max_length=2, db_collation='utf8mb4_general_ci', blank=True, null=True)
    class_field = models.CharField(db_column='Class', max_length=2, db_collation='utf8mb4_general_ci', blank=True, null=True)
    style = models.CharField(db_column='Style', max_length=2, db_collation='utf8mb4_general_ci', blank=True, null=True)
    product_subcategory = models.ForeignKey('ProductionProductSubcategory', models.DO_NOTHING, db_column='ProductSubcategoryID', blank=True, null=True)
    product_model = models.ForeignKey('ProductionProductModel', models.DO_NOTHING, db_column='ProductModelID', blank=True, null=True)
    sell_start_date = models.DateTimeField(db_column='SellStartDate')
    sell_end_date = models.DateTimeField(db_column='SellEndDate', blank=True, null=True)
    discontinued_date = models.DateTimeField(db_column='DiscontinuedDate', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_Product'


class ProductionProductCategory(models.Model):
    product_category_id = models.IntegerField(db_column='ProductCategoryID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductCategory'


class ProductionProductCostHistory(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    standard_cost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductCostHistory'
        unique_together = (('product_id', 'start_date'),)


class ProductionProductDescription(models.Model):
    product_description_id = models.IntegerField(db_column='ProductDescriptionID', primary_key=True)
    description = models.CharField(db_column='Description', max_length=400, db_collation='utf8mb4_general_ci')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductDescription'


class ProductionProductDocument(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    document_node = models.ForeignKey(ProductionDocument, models.DO_NOTHING, db_column='DocumentNode')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductDocument'
        unique_together = (('product_id', 'document_node'),)


class ProductionProductInventory(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    location = models.ForeignKey(ProductionLocation, models.DO_NOTHING, db_column='LocationID')
    shelf = models.CharField(db_column='Shelf', max_length=10, db_collation='utf8mb4_general_ci')
    bin = models.PositiveIntegerField(db_column='Bin')
    quantity = models.SmallIntegerField(db_column='Quantity')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductInventory'
        unique_together = (('product_id', 'location_id'),)


class ProductionProductListPriceHistory(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    list_price = models.DecimalField(db_column='ListPrice', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductListPriceHistory'
        unique_together = (('product_id', 'start_date'),)


class ProductionProductModel(models.Model):
    product_model_id = models.IntegerField(db_column='ProductModelID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    catalog_description = models.TextField(db_column='CatalogDescription', blank=True, null=True)
    instructions = models.TextField(db_column='Instructions', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductModel'


class ProductionProductModelIllustration(models.Model):
    product_model = models.OneToOneField(ProductionProductModel, models.DO_NOTHING, db_column='ProductModelID', primary_key=True)
    illustration = models.ForeignKey(ProductionIllustration, models.DO_NOTHING, db_column='IllustrationID')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductModelIllustration'
        unique_together = (('product_model_id', 'illustration_id'),)


class ProductionProductModelProductDescriptionCulture(models.Model):
    product_model = models.OneToOneField(ProductionProductModel, models.DO_NOTHING, db_column='ProductModelID', primary_key=True)
    product_description = models.ForeignKey(ProductionProductDescription, models.DO_NOTHING, db_column='ProductDescriptionID')
    culture = models.ForeignKey(ProductionCulture, models.DO_NOTHING, db_column='CultureID')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductModelProductDescriptionCulture'
        unique_together = (('product_model_id', 'product_description_id', 'culture_id'),)


class ProductionProductPhoto(models.Model):
    product_photo_id = models.IntegerField(db_column='ProductPhotoID', primary_key=True)
    thumb_nail_photo = models.TextField(db_column='ThumbNailPhoto', blank=True, null=True)
    thumbnail_photo_file_name = models.CharField(db_column='ThumbnailPhotoFileName', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)
    large_photo = models.TextField(db_column='LargePhoto', blank=True, null=True)
    large_photo_file_name = models.CharField(db_column='LargePhotoFileName', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductPhoto'


class ProductionProductProductPhoto(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    product_photo = models.ForeignKey(ProductionProductPhoto, models.DO_NOTHING, db_column='ProductPhotoID')
    primary = models.IntegerField(db_column='Primary')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductProductPhoto'
        unique_together = (('product_id', 'product_photo_id'),)


class ProductionProductReview(models.Model):
    product_review_id = models.IntegerField(db_column='ProductReviewID', primary_key=True)
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    reviewer_name = models.CharField(db_column='ReviewerName', max_length=100, db_collation='utf8mb4_general_ci')
    review_date = models.DateTimeField(db_column='ReviewDate')
    email_address = models.CharField(db_column='EmailAddress', max_length=50, db_collation='utf8mb4_general_ci')
    rating = models.IntegerField(db_column='Rating')
    comments = models.CharField(db_column='Comments', max_length=3850, db_collation='utf8mb4_general_ci', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductReview'


class ProductionProductSubcategory(models.Model):
    product_subcategory_id = models.IntegerField(db_column='ProductSubcategoryID', primary_key=True)
    product_category = models.ForeignKey(ProductionProductCategory, models.DO_NOTHING, db_column='ProductCategoryID')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ProductSubcategory'


class ProductionScrapReason(models.Model):
    scrap_reason_id = models.SmallIntegerField(db_column='ScrapReasonID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_ScrapReason'


class ProductionTransactionHistory(models.Model):
    transaction_id = models.IntegerField(db_column='TransactionID', primary_key=True)
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    reference_order_id = models.IntegerField(db_column='ReferenceOrderID')
    reference_order_line_id = models.IntegerField(db_column='ReferenceOrderLineID')
    transaction_date = models.DateTimeField(db_column='TransactionDate')
    transaction_type = models.CharField(db_column='TransactionType', max_length=1, db_collation='utf8mb4_general_ci')
    quantity = models.IntegerField(db_column='Quantity')
    actual_cost = models.DecimalField(db_column='ActualCost', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_TransactionHistory'


class ProductionTransactionHistoryArchive(models.Model):
    transaction_id = models.IntegerField(db_column='TransactionID', primary_key=True)
    product_id = models.IntegerField(db_column='ProductID')
    reference_order_id = models.IntegerField(db_column='ReferenceOrderID')
    reference_order_line_id = models.IntegerField(db_column='ReferenceOrderLineID')
    transaction_date = models.DateTimeField(db_column='TransactionDate')
    transaction_type = models.CharField(db_column='TransactionType', max_length=1, db_collation='utf8mb4_general_ci')
    quantity = models.IntegerField(db_column='Quantity')
    actual_cost = models.DecimalField(db_column='ActualCost', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_TransactionHistoryArchive'


class ProductionUnitMeasure(models.Model):
    unit_measure_code = models.CharField(db_column='UnitMeasureCode', primary_key=True, max_length=3, db_collation='utf8mb4_general_ci')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_UnitMeasure'


class ProductionWorkOrder(models.Model):
    work_order_id = models.IntegerField(db_column='WorkOrderID', primary_key=True)
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    order_qty = models.IntegerField(db_column='OrderQty')
    stocked_qty = models.IntegerField(db_column='StockedQty')
    scrapped_qty = models.SmallIntegerField(db_column='ScrappedQty')
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    due_date = models.DateTimeField(db_column='DueDate')
    scrap_reason = models.ForeignKey(ProductionScrapReason, models.DO_NOTHING, db_column='ScrapReasonID', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_WorkOrder'


class ProductionWorkOrderRouting(models.Model):
    work_order = models.OneToOneField(ProductionWorkOrder, models.DO_NOTHING, db_column='WorkOrderID', primary_key=True)
    product_id = models.IntegerField(db_column='ProductID')
    operation_sequence = models.SmallIntegerField(db_column='OperationSequence')
    location = models.ForeignKey(ProductionLocation, models.DO_NOTHING, db_column='LocationID')
    scheduled_start_date = models.DateTimeField(db_column='ScheduledStartDate')
    scheduled_end_date = models.DateTimeField(db_column='ScheduledEndDate')
    actual_start_date = models.DateTimeField(db_column='ActualStartDate', blank=True, null=True)
    actual_end_date = models.DateTimeField(db_column='ActualEndDate', blank=True, null=True)
    actual_resource_hrs = models.DecimalField(db_column='ActualResourceHrs', max_digits=9, decimal_places=4, blank=True, null=True)
    planned_cost = models.DecimalField(db_column='PlannedCost', max_digits=19, decimal_places=4)
    actual_cost = models.DecimalField(db_column='ActualCost', max_digits=19, decimal_places=4, blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Production_WorkOrderRouting'
        unique_together = (('work_order_id', 'product_id', 'operation_sequence'),)


class PurchasingProductVendor(models.Model):
    product = models.OneToOneField(ProductionProduct, models.DO_NOTHING, db_column='ProductID', primary_key=True)
    business_entity = models.ForeignKey('PurchasingVendor', models.DO_NOTHING, db_column='BusinessEntityID')
    average_lead_time = models.IntegerField(db_column='AverageLeadTime')
    standard_price = models.DecimalField(db_column='StandardPrice', max_digits=19, decimal_places=4)
    last_receipt_cost = models.DecimalField(db_column='LastReceiptCost', max_digits=19, decimal_places=4, blank=True, null=True)
    last_receipt_date = models.DateTimeField(db_column='LastReceiptDate', blank=True, null=True)
    min_order_qty = models.IntegerField(db_column='MinOrderQty')
    max_order_qty = models.IntegerField(db_column='MaxOrderQty')
    on_order_qty = models.IntegerField(db_column='OnOrderQty', blank=True, null=True)
    unit_measure_code = models.ForeignKey(ProductionUnitMeasure, models.DO_NOTHING, db_column='UnitMeasureCode')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Purchasing_ProductVendor'
        unique_together = (('product_id', 'business_entity_id'),)


class PurchasingPurchaseOrderDetail(models.Model):
    purchase_order = models.OneToOneField('PurchasingPurchaseOrderHeader', models.DO_NOTHING, db_column='PurchaseOrderID', primary_key=True)
    purchase_order_detail_id = models.IntegerField(db_column='PurchaseOrderDetailID')
    due_date = models.DateTimeField(db_column='DueDate')
    order_qty = models.SmallIntegerField(db_column='OrderQty')
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    unit_price = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4)
    line_total = models.DecimalField(db_column='LineTotal', max_digits=19, decimal_places=4)
    received_qty = models.DecimalField(db_column='ReceivedQty', max_digits=8, decimal_places=2)
    rejected_qty = models.DecimalField(db_column='RejectedQty', max_digits=8, decimal_places=2)
    stocked_qty = models.DecimalField(db_column='StockedQty', max_digits=9, decimal_places=2)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Purchasing_PurchaseOrderDetail'
        unique_together = (('purchase_order_id', 'purchase_order_detail_id'),)


class PurchasingPurchaseOrderHeader(models.Model):
    purchase_order_id = models.IntegerField(db_column='PurchaseOrderID', primary_key=True)
    revision_number = models.PositiveIntegerField(db_column='RevisionNumber')
    status = models.PositiveIntegerField(db_column='Status')
    employee = models.ForeignKey(HumanResourcesEmployee, models.DO_NOTHING, db_column='EmployeeID')
    vendor = models.ForeignKey('PurchasingVendor', models.DO_NOTHING, db_column='VendorID')
    ship_method = models.ForeignKey('PurchasingShipMethod', models.DO_NOTHING, db_column='ShipMethodID')
    order_date = models.DateTimeField(db_column='OrderDate')
    ship_date = models.DateTimeField(db_column='ShipDate', blank=True, null=True)
    sub_total = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=4)
    tax_amt = models.DecimalField(db_column='TaxAmt', max_digits=19, decimal_places=4)
    freight = models.DecimalField(db_column='Freight', max_digits=19, decimal_places=4)
    total_due = models.DecimalField(db_column='TotalDue', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Purchasing_PurchaseOrderHeader'


class PurchasingShipMethod(models.Model):
    ship_method_id = models.IntegerField(db_column='ShipMethodID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    ship_base = models.DecimalField(db_column='ShipBase', max_digits=19, decimal_places=4)
    ship_rate = models.DecimalField(db_column='ShipRate', max_digits=19, decimal_places=4)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Purchasing_ShipMethod'


class PurchasingVendor(models.Model):
    business_entity = models.OneToOneField(PersonBusinessEntity, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    account_number = models.CharField(db_column='AccountNumber', unique=True, max_length=30, db_collation='utf8mb4_general_ci')
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb4_general_ci')
    credit_rating = models.PositiveIntegerField(db_column='CreditRating')
    preferred_vendor_status = models.IntegerField(db_column='PreferredVendorStatus')
    active_flag = models.IntegerField(db_column='ActiveFlag')
    purchasing_web_service_u_r_l = models.CharField(db_column='PurchasingWebServiceURL', max_length=1024, db_collation='utf8mb4_general_ci', blank=True, null=True)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Purchasing_Vendor'


class SalesCountryRegionCurrency(models.Model):
    country_region_code = models.OneToOneField(PersonCountryRegion, models.DO_NOTHING, db_column='CountryRegionCode', primary_key=True)
    currency_code = models.ForeignKey('SalesCurrency', models.DO_NOTHING, db_column='CurrencyCode')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_CountryRegionCurrency'
        unique_together = (('country_region_code', 'currency_code'),)


class SalesCreditCard(models.Model):
    credit_card_id = models.IntegerField(db_column='CreditCardID', primary_key=True)
    card_type = models.CharField(db_column='CardType', max_length=50, db_collation='utf8mb4_general_ci')
    card_number = models.CharField(db_column='CardNumber', unique=True, max_length=25, db_collation='utf8mb4_general_ci')
    exp_month = models.PositiveIntegerField(db_column='ExpMonth')
    exp_year = models.SmallIntegerField(db_column='ExpYear')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_CreditCard'


class SalesCurrency(models.Model):
    currency_code = models.CharField(db_column='CurrencyCode', primary_key=True, max_length=3, db_collation='utf8mb4_general_ci')
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_Currency'


class SalesCurrencyRate(models.Model):
    currency_rate_id = models.IntegerField(db_column='CurrencyRateID', primary_key=True)
    currency_rate_date = models.DateTimeField(db_column='CurrencyRateDate')
    from_currency_code = models.ForeignKey(SalesCurrency, models.DO_NOTHING, db_column='FromCurrencyCode')
    to_currency_code = models.ForeignKey(SalesCurrency, models.DO_NOTHING, db_column='ToCurrencyCode')
    average_rate = models.DecimalField(db_column='AverageRate', max_digits=19, decimal_places=4)
    end_of_day_rate = models.DecimalField(db_column='EndOfDayRate', max_digits=19, decimal_places=4)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_CurrencyRate'
        unique_together = (('currency_rate_date', 'from_currency_code', 'to_currency_code'),)


class SalesCustomer(models.Model):
    customer_id = models.IntegerField(db_column='CustomerID', primary_key=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    store = models.ForeignKey('SalesStore', models.DO_NOTHING, db_column='StoreID', blank=True, null=True)
    territory = models.ForeignKey('SalesTerritory', models.DO_NOTHING, db_column='TerritoryID', blank=True, null=True)
    account_number = models.CharField(db_column='AccountNumber', unique=True, max_length=10)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_Customer'


class SalesPersonCreditCard(models.Model):
    business_entity = models.OneToOneField(Person, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    credit_card = models.ForeignKey(SalesCreditCard, models.DO_NOTHING, db_column='CreditCardID')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_PersonCreditCard'
        unique_together = (('business_entity_id', 'credit_card_id'),)


class SalesOrderDetail(models.Model):
    sales_order = models.OneToOneField('SalesOrderHeader', models.DO_NOTHING, db_column='SalesOrderID', primary_key=True)
    sales_order_detail_id = models.IntegerField(db_column='SalesOrderDetailID')
    carrier_tracking_number = models.CharField(db_column='CarrierTrackingNumber', max_length=25, db_collation='utf8mb4_general_ci', blank=True, null=True)
    order_qty = models.SmallIntegerField(db_column='OrderQty')
    product = models.ForeignKey('SalesSpecialOfferProduct', models.DO_NOTHING, db_column='ProductID')
    special_offer = models.ForeignKey('SalesSpecialOfferProduct', models.DO_NOTHING, db_column='SpecialOfferID')
    unit_price = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4)
    unit_price_discount = models.DecimalField(db_column='UnitPriceDiscount', max_digits=19, decimal_places=4)
    line_total = models.DecimalField(db_column='LineTotal', max_digits=38, decimal_places=6)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesOrderDetail'
        unique_together = (('sales_order_id', 'sales_order_detail_id'),)


class SalesOrderHeader(models.Model):
    sales_order_id = models.IntegerField(db_column='SalesOrderID', primary_key=True)
    revision_number = models.PositiveIntegerField(db_column='RevisionNumber')
    order_date = models.DateTimeField(db_column='OrderDate')
    due_date = models.DateTimeField(db_column='DueDate')
    ship_date = models.DateTimeField(db_column='ShipDate', blank=True, null=True)
    status = models.PositiveIntegerField(db_column='Status')
    online_order_flag = models.IntegerField(db_column='OnlineOrderFlag')
    sales_order_number = models.CharField(db_column='SalesOrderNumber', unique=True, max_length=25, db_collation='utf8mb4_general_ci')
    purchase_order_number = models.CharField(db_column='PurchaseOrderNumber', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)
    account_number = models.CharField(db_column='AccountNumber', max_length=30, db_collation='utf8mb4_general_ci', blank=True, null=True)
    customer = models.ForeignKey(SalesCustomer, models.DO_NOTHING, db_column='CustomerID')
    sales_person = models.ForeignKey('SalesPerson', models.DO_NOTHING, db_column='SalesPersonID', blank=True, null=True)
    territory = models.ForeignKey('SalesTerritory', models.DO_NOTHING, db_column='TerritoryID', blank=True, null=True)
    bill_to_address = models.ForeignKey(PersonAddress, models.DO_NOTHING, db_column='BillToAddressID')
    ship_to_address = models.ForeignKey(PersonAddress, models.DO_NOTHING, db_column='ShipToAddressID')
    ship_method = models.ForeignKey(PurchasingShipMethod, models.DO_NOTHING, db_column='ShipMethodID')
    credit_card = models.ForeignKey(SalesCreditCard, models.DO_NOTHING, db_column='CreditCardID', blank=True, null=True)
    credit_card_approval_code = models.CharField(db_column='CreditCardApprovalCode', max_length=15, blank=True, null=True)
    currency_rate = models.ForeignKey(SalesCurrencyRate, models.DO_NOTHING, db_column='CurrencyRateID', blank=True, null=True)
    sub_total = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=4)
    tax_amt = models.DecimalField(db_column='TaxAmt', max_digits=19, decimal_places=4)
    freight = models.DecimalField(db_column='Freight', max_digits=19, decimal_places=4)
    total_due = models.DecimalField(db_column='TotalDue', max_digits=19, decimal_places=4)
    comment = models.CharField(db_column='Comment', max_length=128, db_collation='utf8mb4_general_ci', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesOrderHeader'


class SalesOrderHeaderSalesReason(models.Model):
    sales_order = models.OneToOneField(SalesOrderHeader, models.DO_NOTHING, db_column='SalesOrderID', primary_key=True)
    sales_reason = models.ForeignKey('SalesReason', models.DO_NOTHING, db_column='SalesReasonID')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesOrderHeaderSalesReason'
        unique_together = (('sales_order_id', 'sales_reason_id'),)


class SalesPerson(models.Model):
    business_entity = models.OneToOneField(HumanResourcesEmployee, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    territory = models.ForeignKey('SalesTerritory', models.DO_NOTHING, db_column='TerritoryID', blank=True, null=True)
    sales_quota = models.DecimalField(db_column='SalesQuota', max_digits=19, decimal_places=4, blank=True, null=True)
    bonus = models.DecimalField(db_column='Bonus', max_digits=19, decimal_places=4)
    commission_pct = models.DecimalField(db_column='CommissionPct', max_digits=10, decimal_places=4)
    sales_y_t_d = models.DecimalField(db_column='SalesYTD', max_digits=19, decimal_places=4)
    sales_last_year = models.DecimalField(db_column='SalesLastYear', max_digits=19, decimal_places=4)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesPerson'


class SalesPersonQuotaHistory(models.Model):
    business_entity = models.OneToOneField(SalesPerson, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    quota_date = models.DateTimeField(db_column='QuotaDate')
    sales_quota = models.DecimalField(db_column='SalesQuota', max_digits=19, decimal_places=4)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesPersonQuotaHistory'
        unique_together = (('business_entity_id', 'quota_date'),)


class SalesReason(models.Model):
    sales_reason_id = models.IntegerField(db_column='SalesReasonID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb4_general_ci')
    reason_type = models.CharField(db_column='ReasonType', max_length=100, db_collation='utf8mb4_general_ci')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesReason'


class SalesTaxRate(models.Model):
    sales_tax_rate_id = models.IntegerField(db_column='SalesTaxRateID', primary_key=True)
    state_province = models.ForeignKey(PersonStateProvince, models.DO_NOTHING, db_column='StateProvinceID')
    tax_type = models.PositiveIntegerField(db_column='TaxType')
    tax_rate = models.DecimalField(db_column='TaxRate', max_digits=10, decimal_places=4)
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb4_general_ci')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesTaxRate'
        unique_together = (('state_province_id', 'tax_type'),)


class SalesTerritory(models.Model):
    territory_id = models.IntegerField(db_column='TerritoryID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=100, db_collation='utf8mb4_general_ci')
    country_region_code = models.ForeignKey(PersonCountryRegion, models.DO_NOTHING, db_column='CountryRegionCode')
    group = models.CharField(db_column='Group', max_length=50, db_collation='utf8mb4_general_ci')
    sales_y_t_d = models.DecimalField(db_column='SalesYTD', max_digits=19, decimal_places=4)
    sales_last_year = models.DecimalField(db_column='SalesLastYear', max_digits=19, decimal_places=4)
    cost_y_t_d = models.DecimalField(db_column='CostYTD', max_digits=19, decimal_places=4)
    cost_last_year = models.DecimalField(db_column='CostLastYear', max_digits=19, decimal_places=4)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesTerritory'


class SalesTerritoryHistory(models.Model):
    business_entity = models.OneToOneField(SalesPerson, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    territory = models.ForeignKey(SalesTerritory, models.DO_NOTHING, db_column='TerritoryID')
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SalesTerritoryHistory'
        unique_together = (('business_entity_id', 'territory_id', 'start_date'),)


class SalesShoppingCartItem(models.Model):
    shopping_cart_item_id = models.IntegerField(db_column='ShoppingCartItemID', primary_key=True)
    shopping_cart_id = models.CharField(db_column='ShoppingCartID', max_length=50, db_collation='utf8mb4_general_ci')
    quantity = models.IntegerField(db_column='Quantity')
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    date_created = models.DateTimeField(db_column='DateCreated')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_ShoppingCartItem'


class SalesSpecialOffer(models.Model):
    special_offer_id = models.IntegerField(db_column='SpecialOfferID', primary_key=True)
    description = models.CharField(db_column='Description', max_length=255, db_collation='utf8mb4_general_ci')
    discount_pct = models.DecimalField(db_column='DiscountPct', max_digits=10, decimal_places=4)
    type = models.CharField(db_column='Type', max_length=50, db_collation='utf8mb4_general_ci')
    category = models.CharField(db_column='Category', max_length=50, db_collation='utf8mb4_general_ci')
    start_date = models.DateTimeField(db_column='StartDate')
    end_date = models.DateTimeField(db_column='EndDate')
    min_qty = models.IntegerField(db_column='MinQty')
    max_qty = models.IntegerField(db_column='MaxQty', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SpecialOffer'


class SalesSpecialOfferProduct(models.Model):
    special_offer = models.OneToOneField(SalesSpecialOffer, models.DO_NOTHING, db_column='SpecialOfferID', primary_key=True)
    product = models.ForeignKey(ProductionProduct, models.DO_NOTHING, db_column='ProductID')
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_SpecialOfferProduct'
        unique_together = (('special_offer_id', 'product_id'),)


class SalesStore(models.Model):
    business_entity = models.OneToOneField(PersonBusinessEntity, models.DO_NOTHING, db_column='BusinessEntityID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb4_general_ci')
    sales_person = models.ForeignKey(SalesPerson, models.DO_NOTHING, db_column='SalesPersonID', blank=True, null=True)
    demographics = models.TextField(db_column='Demographics', blank=True, null=True)
    rowguid = models.CharField(unique=True, max_length=64)
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'Sales_Store'


class DboAWBuildVersion(models.Model):
    system_information_id = models.PositiveIntegerField(db_column='SystemInformationID', primary_key=True)
    database_version = models.CharField(db_column='Database Version', max_length=25, db_collation='utf8mb4_general_ci')
    version_date = models.DateTimeField(db_column='VersionDate')
    modified_date = models.DateTimeField(db_column='ModifiedDate')

    class Meta:

        db_table = 'dbo_AWBuildVersion'


class DboDatabaseLog(models.Model):
    database_log_id = models.IntegerField(db_column='DatabaseLogID', primary_key=True)
    post_time = models.DateTimeField(db_column='PostTime')
    database_user = models.CharField(db_column='DatabaseUser', max_length=160)
    event = models.CharField(db_column='Event', max_length=160)
    schema = models.CharField(db_column='Schema', max_length=160, blank=True, null=True)
    object = models.CharField(db_column='Object', max_length=160, blank=True, null=True)
    t_s_q_l = models.TextField(db_column='TSQL', db_collation='utf8mb4_general_ci')
    xml_event = models.TextField(db_column='XmlEvent')

    class Meta:

        db_table = 'dbo_DatabaseLog'


class DboErrorLog(models.Model):
    error_log_id = models.IntegerField(db_column='ErrorLogID', primary_key=True)
    error_time = models.DateTimeField(db_column='ErrorTime')
    user_name = models.CharField(db_column='UserName', max_length=160)
    error_number = models.IntegerField(db_column='ErrorNumber')
    error_severity = models.IntegerField(db_column='ErrorSeverity', blank=True, null=True)
    error_state = models.IntegerField(db_column='ErrorState', blank=True, null=True)
    error_procedure = models.CharField(db_column='ErrorProcedure', max_length=126, db_collation='utf8mb4_general_ci', blank=True, null=True)
    error_line = models.IntegerField(db_column='ErrorLine', blank=True, null=True)
    error_message = models.CharField(db_column='ErrorMessage', max_length=4000, db_collation='utf8mb4_general_ci')

    class Meta:

        db_table = 'dbo_ErrorLog'
