import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent{

  constructor() { }

  sidebarToggle:boolean = false;

  toogle(){
    this.sidebarToggle = !this.sidebarToggle;
  }
}
