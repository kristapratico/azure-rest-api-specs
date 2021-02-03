# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6369, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional

import msrest.serialization


class AnalyzedForm(msrest.serialization.Model):
    """Base model for arbitrary forms. Has an untyped set of fields that can be discovered.

    All required parameters must be populated in order to send to Azure.

    :param doc_type: Required.
    :type doc_type: str
    """

    _validation = {
        'doc_type': {'required': True},
    }

    _attribute_map = {
        'doc_type': {'key': 'docType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        doc_type: str,
        **kwargs
    ):
        super(AnalyzedForm, self).__init__(**kwargs)
        self.doc_type = doc_type


class AnalyzedBusinessCard(AnalyzedForm):
    """AnalyzedBusinessCard.

    All required parameters must be populated in order to send to Azure.

    :param doc_type: Required.
    :type doc_type: str
    :param fields: Required.
    :type fields: ~body_polymorphic.models.AnalyzedBusinessCardFields
    """

    _validation = {
        'doc_type': {'required': True},
        'fields': {'required': True},
    }

    _attribute_map = {
        'doc_type': {'key': 'docType', 'type': 'str'},
        'fields': {'key': 'fields', 'type': 'AnalyzedBusinessCardFields'},
    }

    def __init__(
        self,
        *,
        doc_type: str,
        fields: "AnalyzedBusinessCardFields",
        **kwargs
    ):
        super(AnalyzedBusinessCard, self).__init__(doc_type=doc_type, **kwargs)
        self.fields = fields


class AnalyzedBusinessCardFields(msrest.serialization.Model):
    """AnalyzedBusinessCardFields.

    :param company_name:
    :type company_name: ~body_polymorphic.models.StringFormField
    :param phone_number:
    :type phone_number: ~body_polymorphic.models.StringFormField
    """

    _attribute_map = {
        'company_name': {'key': 'companyName', 'type': 'StringFormField'},
        'phone_number': {'key': 'phoneNumber', 'type': 'StringFormField'},
    }

    def __init__(
        self,
        *,
        company_name: Optional["StringFormField"] = None,
        phone_number: Optional["StringFormField"] = None,
        **kwargs
    ):
        super(AnalyzedBusinessCardFields, self).__init__(**kwargs)
        self.company_name = company_name
        self.phone_number = phone_number


class AnalyzedPassport(AnalyzedForm):
    """AnalyzedPassport.

    All required parameters must be populated in order to send to Azure.

    :param doc_type: Required.
    :type doc_type: str
    :param fields: Required.
    :type fields: ~body_polymorphic.models.AnalyzedPassportFormFields
    """

    _validation = {
        'doc_type': {'required': True},
        'fields': {'required': True},
    }

    _attribute_map = {
        'doc_type': {'key': 'docType', 'type': 'str'},
        'fields': {'key': 'fields', 'type': 'AnalyzedPassportFormFields'},
    }

    def __init__(
        self,
        *,
        doc_type: str,
        fields: "AnalyzedPassportFormFields",
        **kwargs
    ):
        super(AnalyzedPassport, self).__init__(doc_type=doc_type, **kwargs)
        self.fields = fields


class AnalyzedPassportFormFields(msrest.serialization.Model):
    """AnalyzedPassportFormFields.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, ~body_polymorphic.models.FormField]
    :param issuing_country:
    :type issuing_country: ~body_polymorphic.models.StringFormField
    :param first_name:
    :type first_name: ~body_polymorphic.models.StringFormField
    :param passport_number:
    :type passport_number: ~body_polymorphic.models.NumberFormField
    :param expiration_date:
    :type expiration_date: ~body_polymorphic.models.DateFormField
    :param contact_names:
    :type contact_names: ~body_polymorphic.models.ListFormField
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{FormField}'},
        'issuing_country': {'key': 'issuingCountry', 'type': 'StringFormField'},
        'first_name': {'key': 'firstName', 'type': 'StringFormField'},
        'passport_number': {'key': 'passportNumber', 'type': 'NumberFormField'},
        'expiration_date': {'key': 'expirationDate', 'type': 'DateFormField'},
        'contact_names': {'key': 'contactNames', 'type': 'ListFormField'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, "FormField"]] = None,
        issuing_country: Optional["StringFormField"] = None,
        first_name: Optional["StringFormField"] = None,
        passport_number: Optional["NumberFormField"] = None,
        expiration_date: Optional["DateFormField"] = None,
        contact_names: Optional["ListFormField"] = None,
        **kwargs
    ):
        super(AnalyzedPassportFormFields, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.issuing_country = issuing_country
        self.first_name = first_name
        self.passport_number = passport_number
        self.expiration_date = expiration_date
        self.contact_names = contact_names


class FormField(msrest.serialization.Model):
    """FormField.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DateFormField, DictionaryFormField, ListFormField, NumberFormField, StringFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
    }

    _subtype_map = {
        'value_type': {'date': 'DateFormField', 'dictionary': 'DictionaryFormField', 'list': 'ListFormField', 'number': 'NumberFormField', 'string': 'StringFormField'}
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        **kwargs
    ):
        super(FormField, self).__init__(**kwargs)
        self.value_type = None  # type: Optional[str]
        self.precision = precision


class DateFormField(FormField):
    """DateFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    :param value:
    :type value: ~datetime.date
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
        'value': {'key': 'value', 'type': 'date'},
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        value: Optional[datetime.date] = None,
        **kwargs
    ):
        super(DateFormField, self).__init__(precision=precision, **kwargs)
        self.value_type = 'date'  # type: str
        self.value = value


class DictionaryFormField(FormField):
    """DictionaryFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    :param value: Dictionary of :code:`<DictionaryFormField>`.
    :type value: dict[str, ~body_polymorphic.models.DictionaryFormField]
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
        'value': {'key': 'value', 'type': '{DictionaryFormField}'},
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        value: Optional[Dict[str, "DictionaryFormField"]] = None,
        **kwargs
    ):
        super(DictionaryFormField, self).__init__(precision=precision, **kwargs)
        self.value_type = 'dictionary'  # type: str
        self.value = value


class ListFormField(FormField):
    """ListFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    :param value:
    :type value: list[~body_polymorphic.models.FormField]
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
        'value': {'key': 'value', 'type': '[FormField]'},
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        value: Optional[List["FormField"]] = None,
        **kwargs
    ):
        super(ListFormField, self).__init__(precision=precision, **kwargs)
        self.value_type = 'list'  # type: str
        self.value = value


class NumberFormField(FormField):
    """NumberFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    :param value:
    :type value: float
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        value: Optional[float] = None,
        **kwargs
    ):
        super(NumberFormField, self).__init__(precision=precision, **kwargs)
        self.value_type = 'number'  # type: str
        self.value = value


class StringFormField(FormField):
    """StringFormField.

    All required parameters must be populated in order to send to Azure.

    :param value_type: Required. Constant filled by server.  Possible values include: "string",
     "date", "time", "phoneNumber", "float", "integer", "list", "dictionary", "selectionMark".
    :type value_type: str or ~body_polymorphic.models.Value
    :param precision:
    :type precision: float
    :param value:
    :type value: str
    """

    _validation = {
        'value_type': {'required': True},
        'precision': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'value_type': {'key': 'valueType', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'float'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        precision: Optional[float] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(StringFormField, self).__init__(precision=precision, **kwargs)
        self.value_type = 'string'  # type: str
        self.value = value
