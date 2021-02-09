import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserregisterComponent } from './userregister/userregister.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { UserregisterService } from './userregister/userregister.service';
import { UserloginComponent } from './userlogin/userlogin.component';
import { ApiService } from './api.service';
import { AuthenticationService } from './authentication.service';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ReportComponent } from './dashboard/report/report.component';
import { TopnavComponent } from './dashboard/topnav/topnav.component';
import { AdminGuard } from './admin/admin.guard';
import { ProfileComponent } from './user/profile/profile.component';
import { EditprofileComponent } from './user/editprofile/editprofile.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ChartComponent } from './chart/chart.component';
import { ListusersComponent } from './user/listusers/listusers.component';
import { EmployeeprofileComponent } from './user/employeeprofile/employeeprofile.component';
import { FileuploaderComponent } from './work/fileuploader/fileuploader.component';

@NgModule({
  declarations: [
    AppComponent,
    UserregisterComponent,
    UserloginComponent,
    DashboardComponent,
    ReportComponent,
    TopnavComponent,
    ProfileComponent,
    EditprofileComponent,
    SidebarComponent,
    ChartComponent,
    ListusersComponent,
    EmployeeprofileComponent,
    FileuploaderComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [UserregisterService,ApiService,AuthenticationService,AdminGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
