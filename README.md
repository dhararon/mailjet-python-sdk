Mailjet Python SDK
==================

## Instalation :

### Requirements :

Installing Requests is simple with pip, just run this in your terminal :

```
$ pip install requests
```
or, with easy_install:

```
$ easy_install requests
```

### Clone From Github :

	1. Clone this repo into your python project.

```
$ git clone <repo>
```

## Quickstart :

First, make sure that:

* Requests is installed

Let’s get started with some simple examples.

### Create the object :

```python

from MailjetApi import MailjetApi

mailjet =	MailjetApi(
				user 		=	'',
				password 	=	'')
```

### Create contact :

```python

mailjet.create_contact(
			email 	=	'',
			name 	=	'')

```

### List apikey resources :

```python

mailjet.get_apiKey(
			id 	=	'' )

```

### Access a given contactslist resource :

```python

mailjet.view_contactlist(
			contactslist_id 	= 	'' )

```

### Add a new contactslist resource :

```python

mailjet.create_contactlist(
			address 		=	'',
			name 			=	'',
			subscriberCount =	0 )

```

### Add a new listrecipient resource :

```python

mailjet.add_contact_to_list(
			contact_id 	= 	'',
			list_id 	= 	'' )

```

### Send an email :

```python

mailjet.send_email(
			fromm 	= 	'',
			to 		= 	'',
			subject	=	'',
			message	=	'' )

```