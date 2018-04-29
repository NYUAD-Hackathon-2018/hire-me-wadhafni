import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { JobsPage } from '../../pages/jobs/jobs';

/**
 * Generated class for the SearchPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-search',
  templateUrl: 'search.html',
})
export class SearchPage {

  ViewJobs: any;
  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.ViewJobs = JobsPage;
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad SearchPage');
  }

}
