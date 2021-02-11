import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-workassign',
  templateUrl: './workassign.component.html',
  styleUrls: ['./workassign.component.css']
})
export class WorkassignComponent implements OnInit {
  presentvalue:number
  constructor() { }

  ngOnInit(): void {
  }

  onIncrement(){
    this.presentvalue += 1
  }

  onDecrement(){
    this.presentvalue -= 1
  }
}
