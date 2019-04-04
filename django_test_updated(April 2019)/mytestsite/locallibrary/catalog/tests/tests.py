from django.test import TestCase
 
# Create your tests here.
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
    
    def tearDown(self):
        # Clean up run after every test method.
        pass
    
    def test_something_that_will_pass(self):
        self.assertFalse(False)
        
    def test_something_that_will_fail(self):
        self.assertTrue(False)
        
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
        
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)