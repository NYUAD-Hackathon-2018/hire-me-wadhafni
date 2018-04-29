import { Component } from '@angular/core';
// import { NavController } from 'ionic-angular';
import { SearchPage } from '../../pages/search/search';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {

  YourFancyButton: any;
  constructor(){
    this.YourFancyButton = SearchPage;
    }
  // constructor(public navCtrl: NavController) {

  //   }

  }

