#include "construction.hh"
#include "SensitiveDetector.hh"

// Include necessary Geant4 headers
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

// Constructor
MyDetectorConstruction::MyDetectorConstruction()
{}

// Destructor
MyDetectorConstruction::~MyDetectorConstruction()
{}

// Construct method
G4VPhysicalVolume* MyDetectorConstruction::Construct()
{
    // Get NIST material manager
    G4NistManager* nist = G4NistManager::Instance();

    // Define Aluminum material with refractive index
    G4Material* Aluminum = nist->FindOrBuildMaterial("G4_Al");
    G4double energy[2] = {1.239841939*eV/0.2, 1.239841939*eV/0.9};
    G4double rindexAluminum[2] = {1.39, 1.39};
    G4MaterialPropertiesTable* mptAluminum = new G4MaterialPropertiesTable();
    mptAluminum->AddProperty("RINDEX", energy, rindexAluminum, 2);
    Aluminum->SetMaterialPropertiesTable(mptAluminum);

    // Define Uranium material with refractive index
    G4Material* Uranium = nist->FindOrBuildMaterial("G4_U");
    G4double rindexUranium[2] = {1.52, 1.52}; // Example values, please adjust to real ones
    G4MaterialPropertiesTable* mptUranium = new G4MaterialPropertiesTable();
    mptUranium->AddProperty("RINDEX", energy, rindexUranium, 2);
    Uranium->SetMaterialPropertiesTable(mptUranium);

    // Define Iron material with refractive index
    G4Material* Iron = nist->FindOrBuildMaterial("G4_Fe");
    G4double rindexIron[2] = {2.91, 2.91}; // Example values, please adjust to real ones
    G4MaterialPropertiesTable* mptIron = new G4MaterialPropertiesTable();
    mptIron->AddProperty("RINDEX", energy, rindexIron, 2);
    Iron->SetMaterialPropertiesTable(mptIron);

    // Define Plastic material with refractive index
    G4Material* Plastic = nist->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");
    G4double rindexPlastic[2] = {1.58, 1.58}; // Example values, please adjust to real ones
    G4MaterialPropertiesTable* mptPlastic = new G4MaterialPropertiesTable();
    mptPlastic->AddProperty("RINDEX", energy, rindexPlastic, 2);
    Plastic->SetMaterialPropertiesTable(mptPlastic);

    // Define World material
    G4Material* world_mat = nist->FindOrBuildMaterial("G4_AIR");

    // Define World volume
    G4Box* solidWorld = new G4Box("World", 0.5*m, 0.5*m, 0.5*m);
    G4LogicalVolume* logicWorld = new G4LogicalVolume(solidWorld, world_mat, "World");
    G4VPhysicalVolume* physWorld = new G4PVPlacement(0, G4ThreeVector(0., 0., 0.), logicWorld, "World", 0, false, 0, true);

    // Define Slab volume
    G4Box* solidSlab = new G4Box("Slab", 0.4*m, 0.4*m, 0.01*m);
    G4LogicalVolume* logicSlab = new G4LogicalVolume(solidSlab, Uranium, "Slab");
    new G4PVPlacement(0, G4ThreeVector(0., 0., 0.25*m), logicSlab, "Slab", logicWorld, false, 0, true);

    // Define Detector volume
    G4Box* solidDet = new G4Box("Detector", 0.005*m, 0.005*m, 0.01*m);
    G4LogicalVolume* logicDet = new G4LogicalVolume(solidDet, world_mat, "Detector");
    new G4PVPlacement(0, G4ThreeVector(0., 0., 0.49*m), logicDet, "Detector", logicWorld, false, 0, true);

    // Return the physical World
    return physWorld;
}

// ConstructSDandField method
void MyDetectorConstruction::ConstructSDandField()
{
    // Create and assign a sensitive detector
    SensitiveDetector* sensDet = new SensitiveDetector("SensitiveDetector");
    SetSensitiveDetector("Detector", sensDet);
}
