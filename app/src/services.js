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
      },{
      }
    ]

    ns.index = {}
    ns.datasets.forEach(function(d, i){
    	ns.index[d.id] = d
    })

    ns.getDatasetInfo = function (id) {
      return ns.index[id.toLocaleLowerCase()]
    }

    return ns
  }])
