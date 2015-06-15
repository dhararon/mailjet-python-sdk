import requests
import json


class MailjetApi():
	def __init__(self, user='', password='', currentList='', currentUser=''):

		self._user = user
		self._password = password

		self._currentList = currentList
		self._currentUser = currentUser

	@property
	def user(self):
		return self._user

	@user.setter
	def user(self, value):
		self._user = value

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, value):
		self._password = value

	@property
	def currentList(self):
		return self._currentList

	@currentList.setter
	def currentList(self, value):
		self._currentList = value

	@property
	def currentUser(self):
		return self._currentUser

	@currentUser.setter
	def currentUser(self, value):
		self._currentUser = value

	'''
		List apikey resources available for this apikey,
		use a GET request. Alternatively, you may want to add one or more
		filters.
	'''
	def get_apiKey(self, id='', **kwargs):
		url = 'https://api.mailjet.com/v3/REST/apikey/'
		try:
			if len(id) != 0:
				url = url + str(id)
				request = requests.get(url, auth=(self.user, self.password))
				if str(request.status_code) == '200':
					return request.json()
				else:
					result = {'error': 'Your credentials are bad'}
					return result
			else:
				request = requests.get(url, auth=(self.user, self.password))
				if str(request.status_code) == '200':
					return request.json()
				else:
					result = {'error': 'Your credentials are bad'}
					return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result
	'''
		Access a given contactslist resource, use a GET request,
		providing the contactslist's ID value.
	'''
	def view_contactlist(self, contactslist_id=''):
		url = 'https://api.mailjet.com/v3/REST/listrecipient/'
		url = url + str(contactslist_id)
		try:
			request = requests.get(url, auth=(self.user, self.password))
			if str(request.status_code) == '200':
				res = request.json()
				return res
			else:
				result = {'error': 'Your credentials are bad'}
				return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result
	'''
		Add a new contactslist resource with a POST request.
	'''
	def create_contactlist(self, address='', name='', subscriberCount=0):
		url = 'https://api.mailjet.com/v3/REST/contactslist'
		headers = {'Content-Type': 'application/json'}
		data = {}
		data['Address'] = address
		data['Name'] = name
		data['SubscriberCount'] = subscriberCount
		try:
			request = requests.post(
				url,
				auth=(self.user, self.password),
				data=json.dumps(data),
				headers=headers)
			if str(request.status_code) == '201':
				res = request.json()
				self.currentList = res['Data'][0]['ID']
				return res
			else:
				result = {'error': 'Your credentials are bad'}
				return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result
	'''
		Add a new contact resource with a POST request.
	'''
	def create_contact(self, email='', name=''):
		url = 'https://api.mailjet.com/v3/REST/contact'
		headers = {'Content-Type': 'application/json'}
		data = {}
		data['Email'] = email
		data['Name'] = name
		try:
			request = requests.post(
				url,
				auth=(self.user, self.password),
				data=json.dumps(data),
				headers=headers)
			if str(request.status_code) == '201':
				res = request.json()
				self.currentUser = res['Data'][0]['ID']
				return res
			else:
				result = {'error': 'Your credentials are bad'}
				return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result
	'''
		Add a new listrecipient resource with a POST request.
	'''
	def add_contact_to_list(self, contact_id='', list_id=''):
		url = 'https://api.mailjet.com/v3/REST/listrecipient'
		headers = {'Content-Type': 'application/json'}
		data = {}
		data['ContactID'] = str(contact_id)
		data['ListID'] = str(list_id)
		data['IsActive'] = 'True'
		try:
			request = requests.post(
				url,
				auth=(self.user, self.password),
				data=json.dumps(data),
				headers=headers)
			if str(request.status_code) == '201':
				return request.json()
			else:
				result = {'error': 'Your credentials are bad'}
				return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result

	def send_email(self, fromm='', to='', subject='', message=''):
		url = 'https://api.mailjet.com/v3/send/message'
		data = {
			'from': fromm,
			'to': to,
			'subject': subject,
			'text': message	}
		try:
			response = requests.post(
				url,
				auth=(self.user, self.password),
				data=data)
			if str(response.status_code) == '200':
				result = {
					'status': 'ok',
					'message': 'Your email has been send'
				}
				return result
			else:
				result = {
					'status': 'error',
					'message': 'Fail trying to send your email. Check your credentials'
				}
				return result
		except:
			result = {'error': 'Your credentials are bad'}
			return result
