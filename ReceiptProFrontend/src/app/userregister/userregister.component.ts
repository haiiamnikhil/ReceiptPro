import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserregisterService } from './userregister.service';

@Component({
  selector: 'app-userregister',
  templateUrl: './userregister.component.html',
  styleUrls: ['./userregister.component.css']
})

export class UserregisterComponent{

  constructor(private service:UserregisterService, private router:Router) {}

  username: string
  password:string
  confirmpassword:string
  email:string;
  first_name:string
  last_name:string
  gender:string
  emp_id:string
  employ_department:string
  employ_designation:string
  date_joined:string
  shift_id:string
  team_lead_id:string
  team_lead_name:string
  team_lead_mail:string
  company_worker_id:string
  employ_role:string
  appointment_status:string
  user_name:any
  errors:any
  profile_image:File
  users = []


  generateUsername(){
    this.user_name = this.email.split("@",1)
    this.username = this.user_name.toString()
  }

  listUsers(){
    this.service.listUsers().subscribe(data =>this.users=data)
  }

  callbacks(response:any){
    let status = response['status']
    if (status == true){
      this.router.navigate(['/login'])
    }
    else{
      this.errors = status['Errors']
      this.router.navigate(['/register'])
    }
  }

  getFile(event:any){
    if (event.target.files.length > 0){
      this.profile_image = event.target.files[0]
      console.log(this.profile_image)
    }
  }

  registerUser(){
    const uploadData = new FormData();
    uploadData.append('profile_image',this.profile_image,this.profile_image.name)
    uploadData.append("username",this.username)
    uploadData.append("password",this.password)
    uploadData.append("email",this.email)
    uploadData.append("first_name",this.first_name)
    uploadData.append("last_name",this.last_name)
    uploadData.append("gender",this.gender)
    console.log(uploadData)
    this.service.register(uploadData).subscribe(data => this.callbacks(data),error => console.log(error));
  }
}