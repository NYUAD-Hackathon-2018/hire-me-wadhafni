import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { SearchPage } from './search';
import { JobsPage } from '../../pages/jobs/jobs';

@NgModule({
  declarations: [
    SearchPage,
    JobsPage
  ],
  imports: [
    IonicPageModule.forChild(SearchPage),
  ],
})
export class SearchPageModule {}
