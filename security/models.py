from django.db import models


class IP(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.GenericIPAddressField()

	def __str__(self):
		return str(self.address)


class Fingerprint(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	hash = models.TextField()
	ip = models.ForeignKey(IP, on_delete=models.DO_NOTHING, blank=True, null=True)


class BannedFingerprint(models.Model):
	banned_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now=True)
	fingerprint = models.ForeignKey(Fingerprint, on_delete=models.CASCADE)
	expiry = models.DateTimeField(blank=True, null=True)
