import { NgModule } from '@angular/core';
import { Routes, RouterModule} from '@angular/router';
import { AdminGuard } from './admin/admin.guard';
import { DashboardComponent } from './dashboard/dashboard.component';
import { EmployeeprofileComponent } from './user/employeeprofile/employeeprofile.component';
import { ListusersComponent } from './user/listusers/listusers.component';
import { ProfileComponent } from './user/profile/profile.component';
import { UserloginComponent } from './userlogin/userlogin.component';
import { UserregisterComponent } from './userregister/userregister.component';

const routes: Routes = [
  {
    path: 'register',
    component:UserregisterComponent,
  },
  {
    path:'listusers',
    component:ListusersComponent
  },
  {
    path: 'login',
    component:UserloginComponent
  },
  {
    path:'user/dashboard',
    component:DashboardComponent,
    canActivate:[AdminGuard]
  },
  {
    path:'user/profile/:username',
    component:ProfileComponent
  },
  {
    path:'emp-profile/:username',
    component:EmployeeprofileComponent
  },
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
