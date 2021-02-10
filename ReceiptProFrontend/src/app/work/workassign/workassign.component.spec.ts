import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkassignComponent } from './workassign.component';

describe('WorkassignComponent', () => {
  let component: WorkassignComponent;
  let fixture: ComponentFixture<WorkassignComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkassignComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkassignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
