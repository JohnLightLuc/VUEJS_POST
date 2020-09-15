# VUEJS_POST

Comment enregistrer des données dans notre base de donnée avec  VueJs.
Pas trop compliquer que ça enfin, allons-y !

### Etape 1: Importer vuejs et axios

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script> //avec cdn
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

### Etape 2: Code vuejs

      new Vue({
                  el: '#myletter',
                  data: {
                      email: '',
                      isregister: false,
                      codesend:false,
                      result: {'succes': false,'reponse':'' },
                  },
                  delimiters: ["${", "}"],
                  methods: {
                      sendregister: function () {
                          axios.defaults.xsrfCookieName = 'csrftoken'
                          axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                          axios.post('http://127.0.0.1:8000/contact/newsletter/', {
                          email:  this.email,
                              }).then(response => {
                                  console.log(response)
                                  this.codesend = true
                                  this.result= response.data
                                  this.email = ''  
                              })
                              .catch((err) => {
                                  console.log(err)
                                  this.codesend = true
                                  this.result['reponse'] = 'Probleme de connexion !'
                                  this.result['succes'] = false      
                          })
                        }
                     }
              })
              
 ### Etape 3: Et mon fichier views.py
    
    from django.http import JsonResponse
    import json
    from .models import Newsletter
  
 
     def letter(request):
        postdata = json.loads(request.body.decode('utf-8'))
        email = postdata['email']
        succes = False
        try:
            newsletter = Newsletter()
            newsletter.email = email
            newsletter.save()
            succes = True
            reponse = 'Vous avez été bien enregistré!'
        except:
            succes = False
            reponse = "Probleme d'enregistrement !"
        datas = {
            'succes':succes,
            'reponse':reponse,
        }
        return JsonResponse(datas, safe=False)
        
  ### Etape 4:Dans mon fichier html
  
  Et les alertes?
  
      <div v-if="codesend">
           <div v-if="result['succes']" class="alert alert-success" role="alert">
              ${ result['reponse'] }
            </div>
            <div v-if="! result['succes']" class="alert alert-danger" role="alert">
                ${ result['reponse'] }
             </div>
        </div>
        
   Comment recuperer et envoyer les données saisies?
								
		<input v-model='email' name="EMAIL" placeholder="Email" >
		<button v-on:click='sendregister' class="btn sub-btn"><span class="lnr lnr-arrow-right"></span></button>
								
  
  
## Enregistrer une image

### html
	<input v-on:change="handleFileUploaded" ref="file" type="file" style="font-size: 11px;">

### Js 
	 methods: {
		 handleFileUploaded (){
		     this.file = this.$refs.file.files[0];

		 },
		 senddata(){
		     let formData = new FormData();
                     formData.append('file', this.file);
		     axios.defaults.xsrfCookieName = 'csrftoken'
	             axios.defaults.xsrfHeaderName = 'X-CSRFToken' 
		     axios.post(
		     	this.base_url + 'url_path', 
			formData, 
			{
			    headers: {
				'Content-Type': 'multipart/form-data',
			    }
			 }
		      ).then(response => {
			  console.log(response)
		      }).catch((err) => {
                          console.log(err);
                      })
		  },
	}
	  
### views.py

	def save(request):
	   try:
	      image = request.FILES['file']
	      myProfil = model.profile()
	      myProfil.image = image
	      myProfil.save()
	      'statut' = True
	      'message' = "Bien enregistré !" 
	    except:
	    	'statut' = False
	      	'message' = "Problème d'enregistrement !" 
	    
	    data = {
              'statut': statut,
              "message":message,
   	     }

    	    return JsonResponse(data, safe=False)

    


