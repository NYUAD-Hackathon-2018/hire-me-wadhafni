import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the JobsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-jobs',
  templateUrl: 'jobs.html',
})
export class JobsPage {

  job;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.job = 'elena';
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad JobsPage');
    const request = new XMLHttpRequest();
    request.open('GET', 'http://13.232.45.142:8080/getWorkers?loc=Dubai&skill=construction&lang=English', true);
    request.onload = () => {
      
      this.job = 'fabricio';
      console.log('stauts', request.status);
      console.log("response " + request.responseText);
      
      var obj = JSON.parse(request.responseText);
      
      console.log(obj);
    };
    request.send();
  }
}