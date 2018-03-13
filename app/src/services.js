'use strict';

/* Services */

angular.module('app.services', [])

	.factory('datasets', [function(){
    var ns = {}     // namespace
    
    ns.datasets = [
      {
      	id: 'corpus-candidats-linkfluence',
        title: 'Corpus “Candidats présidentielle 2017” sur Linkfluence Radarly',
        licence: 'confidentiel',
        auteurs: 'Linkfluence / Guilhem Fouetillou',
        description: 'Ecoute des réseaux sociaux (Twitter, Instagram, Facebook…)'
      }
    ]

    ns.index = {}
    ns.datasets.forEach(function(d, i){
    	ns.index[d.id] = d
    })

    ns.get = function (id) {
      return ns.index[id.toLocaleLowerCase()]
    }

    ns.getAll = function(options) {
    	options = options || {}

    	if (options.sort && options.sort=='licence') {
    		var sortLicence = function(licence){
    			if (licence == 'confidentiel') {
    				return 'zzz'
    			} else return licence
    		}
    		return ns.datasets.sort(function(a, b){
    			if (a == b) return 0
    			if (sortLicence(a) < sortLicence(b)) return -1
    			return 1
    		})
    	} else return ns.datasets
    }

    return ns
  }])
